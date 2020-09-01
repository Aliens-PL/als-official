import re


#$space (){   or $space() => $FuncCall()
R_EP        = r'^(\s*\$space)([\s\{\}]*)$'
#$133T_5P34K param1 param2 {
R_FUNC_DEF  = r'^(\s*\$(?!space\b)[A-Za-z_][a-zA-Z0-9_]{0,}\s[^\(\)]([\sa-zA-Z_][A-Za-z0-9_ ]*)*)\{*\}*'
#oop keywordds
R_OOP       = r'(^|\b)(\@static|locked|planet|iplanet)\b'
# Variables , declaration + affectation
R_VAR       = r'^(\s*[A-Za-z_])[A-Za-z0-9_]*\s*[+\-*/^&]*\s*\='
# Constant
R_CONST     = r'^(\s*\_\$[A-Za-z_])[A-Za-z0-9_]*\s*[+\-*/~^&]*\s*\='
# Func Calls
F_CALL = r'\s*\$[A-Za-z_0-9]*\s*\((.*)(\)\s*)$'
# Opening / Left symboles
L_SYMBOLE_2 = r'^(\s*[\{\[\(]\s*)'
# Closing / right Symboles
R_SYMBOLE_2 = r'^(\s*[\}\]\)]\s*)'
# IF COND
COND_IF     = r'\s*[^\S\w]if\s*\((.*)\)[\s\{]*'
# ELIF COND
COND_ELIF   = r'\s{0,}\}{0,1}[^\w]\:\s*\((.*)\)[\s\{]{0,1}'
# ELIF COND
COND_ELSE   = r'(\s*\{*\s*:\s*\{{0,1})$'
# LOOPS : @loop()
LOOP_LOOP   = r'(\s*\@{1,1}loop\s{0,}\((.*)\)\s{1,}as\s{1,}[A-Za-z_]{1,1}[A-Za-z_0-9]{0,}\s*\{*)$'
# LOOPS : @while
LOOP_WHILE   = r'(\s*\@{1,1}while\s{0,}\((.*)\)\s*\{*)$'
# Planet Init
P_INIT       = r'^(\s{0,}\${1,1}Init\s{1,1})'
# break from loop
BREAK        = r'(^|\b)break\b'
# One line return
RET         = r'^(\s*return) '

class Parser(object):



    # Recursive Function to get a valid none-py builtin keyword
    # For [vars - consts - functions ] for now atleast .
    # More to come later .
    def __get_valid_py_name(self , Name):
        res = None
        if Name in self.__py_builtins:
            res = self.__get_valid_py_name('_'+Name)
        return res

    def __init__(self , lexDict):
        self.__py_builtins = __import__('keyword').kwlist.extend(dir('__builtins__'))
        self.__out = {}

        self.__fdefs = []
        self.__vars  = []
        
        self.__isDone = True
        self.__output = ""
        
        self.__lex = lexDict
        print("+ Starting Parser ...", end='')
        self.__parse()

        if self.__isDone:
            pass#print(" Done .")
            #print(__import__('json').dumps(self.__out , indent=4 ))
        else:
            print(self.__output)
            exit(0)

    def __set_err(self, er):
        print('\n'+er)
        exit(0)


    def __parse(self):
        if self.__lex != None:
            
            #print(__import__('json').dumps(self.__lex , indent=4 ))
            self.__fdefs = [self.__lex['main'][x][1].strip().lower() for x in self.__lex['main'] if self.__lex['main'][x][0] == 'fdef' ]
            #print(self.__fdefs)
            try:
                
                for line_nbr in self.__lex['main']:
                    if self.__lex['main'][line_nbr] == "empty":
                        self.__out[line_nbr] = "\n"

                    

                    elif isinstance(self.__lex['main'][line_nbr] , list):
                        if self.__lex['main'][line_nbr][0] == 'comment':
                            self.__out[line_nbr] = self.__lex['main'][line_nbr][1]
                        elif self.__lex['main'][line_nbr][0] == 'load':
                            self.__check_loads(self.__lex['main'][line_nbr][1])
                        # check @using
                        elif self.__lex['main'][line_nbr][0] == 'using':
                            pass
                        elif self.__lex['main'][line_nbr][0] == 'var':
                            self.__check_vars( line_nbr, self.__lex['main'][line_nbr][1])                        
                        elif self.__lex['main'][line_nbr][0] == 'fcall':
                            self.__check_fcall( line_nbr, self.__lex['main'][line_nbr][1])
                        elif self.__lex['main'][line_nbr][0] == 'fdef':
                            self.__check_fdef(line_nbr , self.__lex['main'][line_nbr][1])

            except Exception as ex:
                print('\n'+str(ex))

        else:
            self.__set_err("+ Parser Failed due to Inteception or code fail .")


    def __check_closing_symbole(self , line_nbr , symbole = '{'):
        start_line = line_nbr

        symb_dico = {
            '{':'}',
            '[':']',
            '(':')'
        }
        _sum  = 0

        while True:
            if line_nbr in self.__lex['main'].keys() :
                if self.__lex['main'][line_nbr][0] not in ['var' , 'const' , 'comment', 'empty'] :
                    #if self.__lex['main'][line_nbr][0] == 'cond_elif':
                        # if self.__lex['main'][line_nbr][1].strip()[0] == symb_dico[symbole]:
                        #     _sum -= 1
                    for a in self.__lex['main'][line_nbr][1].strip() :
                        if a == symbole:
                            _sum += 1
                        elif a == symb_dico[symbole]:
                            _sum -= 1
                            if _sum == 0:
                                return line_nbr


            else:
                print("+ Could not Find the closing { for the } in line "+ str(start_line))
                exit(0)

            line_nbr += 1

    def __check_fdef(self, line_nbr , line):
        strp_line = line.strip()
        last_s = strp_line[-1]
        _lnbr = line_nbr


        if last_s != '{':
            _lnbr += 1
            last_s = self.__lex['main'][_lnbr][1].strip()

            
        if last_s == '{':
            _nm = strp_line[1:]

            self.__out[line_nbr] = [
                'fdef',
                {
                    'line':strp_line,
                    'block_start': line_nbr,
                    'block_end': self.__check_closing_symbole(_lnbr)            
                }
            ]

        else:
            #print(self.__out)
            print(f"+ Invalid Function Deffinition at {line_nbr}")
            exit(0)

    def __check_fcall(self, line_nbr , line):

        val = line.strip()
        val = val[0:val.index('(')]
        if val == "$als_official":
            print("""          ...-...                                
                          ...-... ..-...                              
                       .-..            .--                            
                     ...     .....        .-                          
                    -       -..  .-.        -.                        
                   -.      -       -         .-                       
                   -      .-.....  .-         .-                      
                   -       . .. .-.*.          .-                     
                  ..  ........-.-.--            ..                    
                   -....       . ......          -                    
                    *                   ..      ..                    
                    ++-            .-*-.  .-.   -                     
                    *+++         -+++++++   -- .                      
                    *++++       +++++++++.   +-                       
                    .++++-     ++++++++++   *++.                      
                     +++++    ++++++++++-  .++++ .                    
                     +++++   .+++++++++.   ++++++ .                   
                     .*++.   -+++++++*    +++++++*                    
                      .        -+++-     .++++++++..                  
                      ..               .-  .*++++++.                  
                       -.             ..       .-**.                  
                        -.         .-.                               
                         ..       ...                                 
                          .-.....-.                                   
                            ....                   

                 
          _      _____ ______ _   _  _____            _____  _      
    /\   | |    |_   _|  ____| \ | |/ ____|          |  __ \| |     
   /  \  | |      | | | |__  |  \| | (___    ______  | |__) | |     
  / /\ \ | |      | | |  __| | . ` |\___ \  |______| |  ___/| |      
 / ____ \| |____ _| |_| |____| |\  |____) |          | |    | |____ 
/_/    \_\______|_____|______|_| \_|_____/           |_|    |______| v0.1

+ Github    : https://github.com/AliensPL/als-official
+ Made by   : @samoray1998 , @AdilMERZ , @x544D , @Mahmoud_Omrani
+ Note      : This is still not even fully functional , the main idea of this is,
              To Provide Our Idea , we Had litteraly no time to finish all this ,
              Since we only worked as 3 of us , But we will keep pushing it to the top :D .

""")
        elif val == "$system":
            # print(line)
            __import__('os').system(str(line.strip()[len(val)+1:line.strip().index(')')]))
        elif val == "$out":
            c = str(line.strip()[len(val)+1:line.strip().index(')')])
            if c.strip()[0] in ['"', "'"]:
                print(c[1:-1].replace("\\n" , '\n'))
            elif '+' in c.strip() and c.strip().split('+').__len__() == 2:
                _tst = c.strip().split('+')
                if re.match(r'\d', _tst[0]) and re.match(r'\d', _tst[1]):
                    if isinstance(_tst[0] , int) or isinstance(_tst[1], int):
                        print(int(_tst[0]) + int(_tst[1]))
                    else:
                        print(float(_tst[0]) + float(_tst[1]))

            elif '-' in c.strip() and c.strip().split('-').__len__() == 2:
                _tst = c.strip().split('-')
                if re.match(r'\d', _tst[0]) and re.match(r'\d', _tst[1]):
                    if isinstance(_tst[0] , int) or isinstance(_tst[1], int):
                        print(int(_tst[0]) - int(_tst[1]))
                    else:
                        print(float(_tst[0]) - float(_tst[1]))

            elif '/' in c.strip() and c.strip().split('/').__len__() == 2:
                _tst = c.strip().split('/')
                if re.match(r'\d', _tst[0]) and re.match(r'\d', _tst[1]):
                    if _tst[1].strip() == '0':
                        self.__set_err(f"+ You can not Devide by 0  at line {line_nbr}")

                    if isinstance(_tst[0] , int) or isinstance(_tst[1], int):
                        print(int(_tst[0]) / int(_tst[1]))
                    else:
                        print(float(_tst[0]) / float(_tst[1]))

            elif '*' in c.strip() and c.strip().split('*').__len__() == 2:
                _tst = c.strip().split('*')
                if re.match(r'\d', _tst[0]) and re.match(r'\d', _tst[1]):
                    if _tst[1].strip() == '0':
                        self.__set_err(f"+ You can not Devide by 0  at line {line_nbr}")
                        
                    if isinstance(_tst[0] , int) or isinstance(_tst[1], int):
                        print(int(_tst[0]) * int(_tst[1]))
                    else:
                        print(float(_tst[0]) * float(_tst[1]))

        elif val == "$in":
            print("+ errr , Sorry Human ! Your variable was Devoured by the black hole :< ")
            exit(0)
        elif not self.__check_presence(val , 'f'):
            self.__set_err(f"+ [{val}] use of undefined Function at line : {line_nbr} .")
        else:
            print("good")

    def __check_vars(self, line_nbr , load_dico):
        stripped_name = re.sub(r'\s', '', load_dico['name'])
        #print(self.__fdefs)
        # vars that has += -= *= /= |= ^= &=
        #if re.search(r'(.*)[\+\-\\\*\&\|\^\~]\s*' , stripped_name):
        val = load_dico['value'].strip()
        if re.search(F_CALL , val):
            val = val[0:str(val).index('(')]
            if not self.__check_presence(val , 'f'):
                self.__set_err(f"+ [{val}] use of undefined Function at line : {line_nbr} .")
            else:
                # valid fcall
                pass

        
    def __check_presence(self, _of , _type):
        if _type == 'f':
            for fdef in self.__fdefs:
                if _of == fdef[0:fdef.index(' ')]:
                    return True
            return False

        else:
            self.__set_err("+ Unknown Presence check error .")
               
            

    def __check_loads(self , load_dico):
        if load_dico['type'] == '@':
            self.__set_err("+ Import Table is not implemented yet")
        elif load_dico['type'] == '_':
            if not __import__('os').path.exists(load_dico['source']):
                self.__set_err(f"+ {load_dico['source']} Is not a valid Path .")
        elif load_dico['type'] == 'http_d':
            if not __import__('os').path.exists(load_dico['source']):
                pass
        else :
            self.__set_err("+ UNKNOWN Loading , probably the code was Tampered with .")
            





