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
        
        self.__isDone = True
        self.__output = ""
        
        self.__lex = lexDict
        print("+ Starting Parser ...", end='')
        self.__parse()

        if self.__isDone:
            print(" Done .")
            #print("+ Executing the Script now ... ")
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

            except Exception as ex:
                print('\n'+str(ex))

        else:
            self.__set_err("+ Parser Failed due to Inteception or code fail .")


    def __check_fcall(self, line_nbr , line):

        val = line.strip()
        val = val[0:val.index('(')]
        if not self.__check_presence(val , 'f'):
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
            pass
        elif load_dico['type'] == '_':
            pass
        elif load_dico['type'] == 'http_d':
            pass
        else :
            self.__set_err("+ UNKNOWN Loading , probably the code was Tampered with .")
            





