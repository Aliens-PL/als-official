import re , os.path

#---TO DO--------------------------------------------------------------------------------#

#- Replace f_call_fixer => Call bin->fixer/updater to fix the last exception logged/cached

#----------------------------------------------------------------------------------------#




class Lexer(object):


    def __init__(self , fileName , abs_file_path):
        # TO DO ####
        # - Check if it's a valid Als Project
        # - Do general Check if Python3 installed before calling this (using c binary instead then invoke this) 
        # - Do check here in python if all the modules used are available , else download them .
        ###########
        self.ALPHABESTS_ = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_'
        self.__py_builtins = __import__('keyword').kwlist.extend(dir('__builtins__'))
        self.abs_file_path = abs_file_path
        self.__lines    = None
        self.__vext     = ['als', 'wals', 'mals'] # valid extensions
        self.__dico     = {}
        self.__dico['loads'] = []
        self.__dico['ep'] = None

        try:
            print("+ Starting Lexer ...")
            if not os.path.exists(abs_file_path+fileName):
                print("+ File Not found !")
                exit(0)

            entry_file = __import__('glob').glob(abs_file_path+fileName)[0]

            if  entry_file and '.' in entry_file:
                self.__dico['ext'] = entry_file.split('.')[-1]
                self.__dico['file'] = abs_file_path+fileName

                print("[+] Processing ... "+entry_file)
                _f = open(abs_file_path+fileName)
                self.__lines = _f.readlines()
                _f.close()

                self.__Initiate()
            else:
                print("404 NOT Found !")     
        except IndexError as x:
            print("Exception Happend : " + str(x))
        except AssertionError as x:
            print("Exception Happend : " + str(x))
 

    def __RegExCheck(self, line, ch):
        #$space (){   or $space() => $FuncCall()
        R_EP        = r'^(\s*\$space\s*\(.*\)\s*)(\=\>|\{*)'
        #$133T_5P34K param1 param2 {
        R_FUNC_DEF  = r'^(\s*\$[A-Za-z_])[A-Za-z0-9_]*\s+[^\(\)][\w\_\s]+\s*\{*'
        #oop keywordds
        R_OOP       = r'(^|\b)(\@static|locked|planet|iplanet)\b'
        # Variables , declaration + affectation
        R_VAR       = r'^(\s*[A-Za-z_])[A-Za-z0-9_]*\s*[+\-*/~^&]*\s*\='
        # Constant
        R_CONST     = r'^(\s*\_\$[A-Za-z_])[A-Za-z0-9_]*\s*[+\-*/~^&]*\s*\='
        # Func Calls
        F_CALL = r'\$[A-Za-z_][A-Za-z0-9_]*\s*\('
        # Opening / Left symboles
        L_SYMBOLE_2 = r'^(\s*[\{\[\(]\s*)'
        # Closing / right Symboles
        R_SYMBOLE_2 = r'^(\s*[\}\]\)]\s*)'
        # One line return
        RET         = r'^(\s*return) '
        
        if ch == 'ep':
            _find_ep = list(re.finditer(R_EP , line , re.IGNORECASE))
            if _find_ep : 
                if _find_ep.__len__() > 1:
                    print("+ Entry Point duplicated !")
                    exit(0)
                else:
                    return _find_ep[0]

            else:
                return None
        elif ch == 'fdef':
            #_find_ep = list(re.finditer(R_FUNC_DEF , line , re.IGNORECASE))
            if re.search(R_FUNC_DEF , line , re.IGNORECASE):
                return True
            return False
        elif ch == 'ret':
            return True if re.search(RET, line , re.IGNORECASE) else False
        elif ch == 'oop':
            for a in line.strip().split(' '):
                if re.search(R_OOP , a , re.IGNORECASE):
                    return True
            return False
        elif ch == 'var':
            return True if re.search(R_VAR, line ) else False

        elif ch == 'const':
            return True if re.search(R_CONST, line ) else False

        elif ch == 'cond':
            return False

        elif ch == 'fcall':
            return True if re.search(F_CALL, line , re.IGNORECASE) else False
            
        elif ch == 'loop':
            return False
            
        elif ch == 'pinit':
            return False 

        elif ch == 'lsymbole_2':
            return True if re.search(L_SYMBOLE_2, line) else False

        elif ch == 'rsymbole_2':
            return True if re.search(R_SYMBOLE_2, line) else False

        else:
            print("+ [ALS_ERROR] Invalid Keyword Given .")
            exit(0)

    def __checkValidName(self, _str , extra_chars=''):
        valid = self.ALPHABESTS_+extra_chars
        for ch in _str:
            if ch not in valid:
                return False
        return True
        
    # Recursive Function to get a valid none-py builtin keyword
    # For [vars - consts - functions ] for now atleast .
    # More to come later .
    def __get_valid_py_name(self , Name):
        res = None
        if Name in self.__py_builtins:
            res = self.__get_valid_py_name('_'+Name)
        return res

    def __header_checks(self , line , line_nbr):
        splitted_load_line = line.strip().replace('\t', ' ').split(' ')
        

        
        # from x laod y Syntax
        if 'from' in line:
            self.__can_using = True
            ''' GENERAL CASES:

            from '../../fileName' load PlanetA --> fileName.als
            from 'http://....file.als' load PlanetA
            from @base load @covert, @web
            '''
            
            if len(splitted_load_line) >= 4 and splitted_load_line[0] == 'from' and splitted_load_line[2] == 'load': #valid loading
                _modSrc         = splitted_load_line[1]
                TmpLsMdNames    = ''.join(splitted_load_line[3:]).replace(' ','').split(',')
                
                # External Modules
                if 'http://' in splitted_load_line[1] or 'https://' in splitted_load_line[1]:
                    for md in TmpLsMdNames:
                        if self.__checkValidName(md) == False:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                            exit(0)

                    self.__dico['main'][line_nbr] = ['load',{'modules':TmpLsMdNames, 'source':_modSrc, 'type':'http'}]
                    self.__dico['loads'].append(line_nbr)
                    #loaded_modules[line_nbr] = [TmpLsMdNames, _modSrc, 'http']
                    #module_indx += 1
                
                # @Modules
                elif splitted_load_line[1][0] == '@':
                    for md in TmpLsMdNames:
                        if md[0] != '@':
                            #f_call_fixer
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module "+md+" Missing @ ?")
                            exit(0)
                    
                        # Checking if it is a valid name
                        # alpha + _ + @
                        elif self.__checkValidName(md[1:]) == False:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                            exit(0)
                        
                    self.__dico['main'][line_nbr] = ['load',{'modules':TmpLsMdNames, 'source':_modSrc, 'type':'@'}]
                    self.__dico['loads'].append(line_nbr)

                
                # Normal Modules
                else:
                    for md in TmpLsMdNames:
                        if self.__checkValidName(md) == False:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                            exit(0)

                    self.__dico['main'][line_nbr] = ['load',{'modules':TmpLsMdNames, 'source':_modSrc, 'type':'_'}]
                    self.__dico['loads'].append(line_nbr)


            else:   
                #invalid loading
                print("[LINE:"+str(line_nbr+1)+"] - Invalid Loading at : \n"+line)#f_call_fixer
                exit(0)

        # load ModuleName 
        elif 'load' in line:
            self.__can_using = True
            ''' GENERAL CASES:

            load ClassA -->  ClassA is ClassA.als (casing does not matters) must have Planet ClassA
            load @base
            '''
            splitted_load_line = line.strip().split(' ')
            if len(splitted_load_line) >= 2 and splitted_load_line[0] == 'load': #valid loading
                TmpLsMdNames    = ''.join(splitted_load_line[1:]).replace(' ','').split(',')

                # case : load @base
                if splitted_load_line[1][0] == '@':
                    for md in TmpLsMdNames:
                        if md[0] != '@':
                            #f_call_fixer
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module "+md+" Missing @ ?")
                            exit(0)
                        
                        # Checking if it is a valid name
                        # alpha + _ + @
                        elif self.__checkValidName(md[1:]) == False:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                            exit(0)

                    self.__dico['main'][line_nbr] = ['load',{'modules':TmpLsMdNames, 'source':None, 'type':'@'}]
                    self.__dico['loads'].append(line_nbr)

                
                # case load modName
                else:
                    for md in TmpLsMdNames:
                        if self.__checkValidName(md) == False:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                            exit(0)

                    self.__dico['main'][line_nbr] = ['load',{'modules':TmpLsMdNames, 'source':self.abs_file_path, 'type':'_'}]
                    self.__dico['loads'].append(line_nbr)

            else:
                print("[LINE:"+str(line_nbr+1)+"] - Invalid Loading at : \n"+line)#f_call_fixer
                exit(0)

        # TODO : Check syntax validity
        elif 'using' in line:
            if self.__can_using:
                self.__dico['main'][line_nbr] = ['using', line]
            else:
                print(f"+ [L:{line_nbr}] 'using' Must be used right after loadings block !")
                exit(0)

        # User Not Allowed to Load anymore , since he started coding
        # Which means basically once some codes other than loading shows up , that means no loading possible
        # So the loading always must be at top !
        #
        # This else will Set the can_load to False so the next lines are only for code that is not for loading
        else:
            # ret False if the line is not a loading syntax
            return  False

        # return True if user can still load
        return True

    def __DotAls(self):
        '''This is For .als Files'''
        can_load        = True

        if self.__lines != None:
            self.__dico['main'] = {}
            # EntryPoint Line Number for easy access
            self.__dico['ep'] = None 
            self.__can_using = False
            self.__cond_started = 0
            self.__cond_ended   = 0
            for line_nbr , original_line in enumerate(self.__lines):
                line = original_line.lower()

                # Empty Lines + comments
                # or 
                # Get all Loads
                # check for \s* lines
                if line.strip() in ['', ' ', '\n', '\t']: # optimize that
                    self.__dico['main'][line_nbr] = 'empty'
                # check for comment lines
                elif line.strip().startswith("#"):
                    self.__dico['main'][line_nbr] = ["comment", line]
                
                # Store valid Functions Defs .
                elif self.__RegExCheck(line, 'fdef'):
                    if self.__dico['ep'] == None:
                        self.__dico['main'][line_nbr] = ['fdef', line]
                    else:
                        print(f"+ [L:{line_nbr+1}] Functions Definitions are not Allowed inside $space() !")
                        exit(0)
                elif self.__RegExCheck(line, 'ret'):
                    self.__dico['main'][line_nbr] = ['ret', line]
                # 3 - Check if variable
                elif self.__RegExCheck(line, 'var'):
                    var_parts = line.split("=")

                    # CHeck of validity of var
                    if var_parts.__len__() == 2:
                        if re.sub(r'\s+', '', var_parts[1]) in [None, '']:
                            print(f"+ [L:{line_nbr+1}] Invalid Variable Affectation !")
                            exit(0)

                        self.__dico['main'][line_nbr] = ['var',
                            {
                                'name':var_parts[0],
                                # this value it can be enything even a fucntion call ,
                                # We dont care about that in Lexer , but we do in Parser
                                'value':var_parts[1]
                            }
                        ]
                    else:
                        print(f"+ [L:{line_nbr+1}] Invalid Variable Declaration !")
                        exit(0)

                # 4 - Check if constant
                elif self.__RegExCheck(line, 'const'):
                    var_parts = line.split("=")

                    # CHeck of validity of var
                    if var_parts.__len__() == 2:
                        if re.sub(r'\s+', '', var_parts[1]) in [None, '']:
                            print(f"+ [L:{line_nbr+1}] Invalid Variable Affectation !")
                            exit(0)

                        self.__dico['main'][line_nbr] = ['const',
                            {
                                'name':var_parts[0],
                                # this value it can be enything even a fucntion call ,
                                # We dont care about that in Lexer , but we do in Parser
                                'value':var_parts[1]
                            }
                        ]
                    else:
                        print(f"+ [L:{line_nbr+1}] A constant should be set to a value at Declaration time !")
                        exit(0)
                        
                # TODO => Check index out of range errs
                elif  can_load:
                    # Check validity of loading syntax + if 'using' keyword there .
                    can_load = self.__header_checks(line, line_nbr)
                    if not can_load:
                        self.__check_keywords(line, line_nbr)


                # this else will handle everything else
                #       L E T S   G 0 !
                else:
                    # Check if there an unothorized load
                    if 'load' in line or 'from' in line:
                        print(f"+ [L:{line_nbr+1}]Modules loading always must be on Top of the code !")
                        exit(0)
                    
                    if 'using' in line :
                        print(f"+ [L:{line_nbr+1}] 'using' must be used Right after loading ends .")
                        exit(0)
                    # Since we are handling .als :
                    # - There should be a $space { } <-- entry point
                    # - No $Function Deffinition inside $space()
                    # - No Planet / IPlanet or oop stuff
                    
                    # Check if it's an entryPoint
                    # if self.__RegExCheck(line, 'ep') != None:
                    #     if self.__dico['ep'] != None:
                    #         print("+ Entry Point $space() Duplicated at : "+ str(line_nbr))
                    #         exit(0)
                    #     else:
                    #         self.__dico['ep'] = str(line_nbr)
                    #         self.__dico['main'][line_nbr] = ['ep',line]
                    
                    #
                    # Now we're Inside $space()
                    #

                    self.__check_keywords(line, line_nbr)
                    
            #-------------------------------#
            #       TEST TOKENS             #
            #        DELETE AFTER           #
            #_______________________________#

            print("+ Done !")
            if self.__dico['ep'] :
                print(__import__('json').dumps(self.__dico , indent=4))
                
                # Loop through  loads and check the syntaxt
                for load_id in self.__dico['loads']:
                    # get the actual load dict infos
                    current_load = self.__dico['main'][load_id][1]
                    if current_load["type"] == "http":
                        print(self.__get_http_load(current_load["source"]))



            else:
                print("+ No EntryPoint found !")

            ################################

        else:
            print("+ Not Valid .als File !")
            exit(0)

    def __get_random_string(self):
        letters = self.ALPHABESTS_
        return ''.join( __import__('random').choice(letters) for i in range(10))


    def __get_http_load(self, link):
        res = None
        rfp = os.path.join(self.abs_file_path, f'mals/externals/loads.sals')

        if os.path.exists(rfp) and link not in open(rfp, 'r').readlines():
        
            print(f"~ Trying to get the [{link}] Module .")
            try:
                resp = __import__('requests').get(link , headers= {'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36 Edg/84.0.522.63'})
                if resp.status_code == 200:
                    res = resp.text
                    print(f"+ Downloaded Successfully .")

                else:
                    print(f"+ HttpResponse returned {resp.status_code} while trying to load [{link}]")
                    exit(0)

            except Exception:
                print(f"+ Failed Retrieving the mals File from : {link}")
                exit(0)

            strn = self.__get_random_string()
            f = open(rfp , 'a+')
            f.write(f"\n{link}::{strn}")
            f.close()



        else:
            print("+ Wrong Als Project .")
            exit(0)

    def __check_keywords(self, line , line_nbr):
        if self.__RegExCheck(line, 'ep') != None:
            if self.__dico['ep'] != None:
                print(f"+ Entry Point Already found at {int(self.__dico['ep'])+1} Duplicated at : {str(line_nbr+1)} ")
                exit(0)
            else:
                self.__dico['ep'] = str(line_nbr)
                self.__dico['main'][line_nbr] = ['ep',line]
        

        # 2 - Check if it's an OOP keyword used in .als

        elif self.__RegExCheck(line, 'oop'):
            print(f"+ [L:{line_nbr+1}] OOP keywords are not allowed in .als Files , Please use .mals for that !")
            exit(0)



        # 5 - Check if condition start
        # elif self.__RegExCheck(line, 'cond_s'):
        #     self.__cond_started += 1

        #     self.__dico['main'][line_nbr] = [
        #         self.__cond_started,
        #         'cond_s',
        #         {
        #             'if'
        #         }
        #     ]

        # 6 - Check if it's a function call
        elif self.__RegExCheck(line, 'fcall'):
            self.__dico['main'][line_nbr] = [
                'fcall',
                line
            ]

        # 7 - Check if it's a loop
        #elif self.__RegExCheck(line, 'loop'):
        #    pass

        # 8 - Check if it's a Plante
        #elif self.__RegExCheck(line, 'pinit'):
        #    pass
        
        # 9 - Check if it's an odd Symbole
        elif self.__RegExCheck(line, 'lsymbole_2'):
            self.__dico['main'][line_nbr] = [
                'lsymbole_2',
                line
            ]

        # 10 - Check if it's an even Symbole
        elif self.__RegExCheck(line, 'rsymbole_2'):
            self.__dico['main'][line_nbr] = [
                'rsymbole_2',
                line
            ]


        else:
            print(f"[-] Unknown ALS Syntax at Line:{line_nbr}\n[>] {line}")
            exit(0)

    def __DotWals(self):
        print("+ Detected WebAls File !")

    def __DotMals(self , file_ = None):
        if file_ == None:
            file_ = self.__dico['file']
        else:
            # Checking if it actually exists Because we're not invoking __DotMals from Lexer() which wont check the existance .
            # Basically we invoked it manually 
            if not os.path.exists(file_):
                print(f"+ Module {file_} Not found ..!")
                exit(0)

        print(f"+ Processing ModuleAls File : {file_} !")
        _fwls = open(file_ , 'r+')
        __lines = _fwls.readlines()
        _fwls.close()
        
        if __lines.__len__() != 0:
            can_load = True
            for line_nbr , original_line in enumerate(self.__lines):
                line = original_line.lower()

                # Empty Lines
                if line.strip() in ['', ' ', '\n', '\t']: # optimize that
                    self.__dico['main'][line_nbr] = 'empty'
                elif line.strip().startswith("#"):
                    self.__dico['main'][line_nbr] = ["comment", line]

                # Get all Loads
                # TODO => Check index out of range errs
                elif can_load:
                    can_load = self.__header_checks(line, line_nbr)

                # this else will handle everything else
                #       L E T S   G 0 !
                else:
                    # Check if there an unothorized load
                    if 'load' in line or 'from' in line:
                        print("+ Modules loading always must be on Top of the code !")
                        exit(0)
                    
                    if 'using' in line :
                        print(f"+ [L:{line_nbr}] 'using' must be used Right after loading ends .")

        else:
            print("+ ModuleAls {file_} Seems to be Empty .")

        
    



    # TO DO ##########
    #
    #  - Loads that uses '...'  , quotes must be handled
    #  -  
    #


    def __Initiate(self):
        '''         + Extensions :  [.mals] are Modules (to be imported only)
                    + Extensions :  [.wals] are webPage Project does not need any imports
                    + Extensions :  [.als]  are Compiled / can not be imported / can use @WebPage module and other Modules\n
            

                    + [.als]    always starts with space {}\n
                    + [.mals]   Does not have space{} and only can have Planet (class) / IPlanet (abstract class)\n
                    + [.wals]   Always starts with $WebPage() kima dar Adil\n 
                    

                    + Checks of other Imported Modules are made on Parser Side.
                    + Now we only care about generating the tokens while doing some easy small checks
                    
        '''

        ##------------------##
        # باِسم اَلـــاــــه  #
        #____________________#
        
        if self.__dico['ext']   == 'als':
            self.__DotAls()

        elif self.__dico['ext'] == 'mals':
            self.__DotMals()
        
        elif self.__dico['ext'] == 'wals':
            self.__DotWals()
        else:
            print("+ Invalid ALS file "+self.__dico['ext'])