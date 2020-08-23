import re

#---TO DO--------------------------------------------------------------------------------#

#- Replace f_call_fixer => Call bin->fixer/updater to fix the last exception logged/cached

#----------------------------------------------------------------------------------------#




class Lexer(object):


    def __init__(self , fileName , abs_file_path):
        self.abs_file_path = abs_file_path
        self.__lines    = None
        self.__vext     = ['als', 'wals', 'mals'] # valid extensions
        self.__dico     = {}

        try:
            print("+ Starting Lexer ...")
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
        if ch == 'mf':
            pass

    def __checkValidName(self, _str , extra_chars=''):
        valid = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_"+extra_chars
        for ch in _str:
            if ch not in valid:
                return False
        return True
        


    def __DotAls(self):
        '''This is For .als Files'''
        can_load        = True
        loaded_modules  = {} # 0:[noduleName, from , type] -> type is one of : _ (local) , @ (built-in), http (link)
        module_indx     = 0

        if self.__lines != None:
            self.__dico['c0de'] = []

            for line_nbr , original_line in enumerate(self.__lines):
                line = original_line.lower()

                # Empty Lines
                if line.strip() in [' ', '\n', '\t']: # optimize that
                    self.__dico['c0de'].append({line_nbr:'empty_line'})

                # Get all Loads
                elif can_load:
                    splitted_load_line = line.strip().replace('\t', ' ').split(' ')
                    # from x laod y Syntax
                    if 'from' in line:
                        
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

                                loaded_modules[module_indx] = [TmpLsMdNames, _modSrc, 'http']
                                module_indx += 1
                            
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
                                    
                                loaded_modules[module_indx] = [TmpLsMdNames, _modSrc, '@']
                                module_indx += 1
                            
                            # Normal Modules
                            else:
                                for md in TmpLsMdNames:
                                    if self.__checkValidName(md) == False:
                                        print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                                        exit(0)

                                loaded_modules[module_indx] = [TmpLsMdNames, _modSrc, '_']
                                module_indx += 1

                        else:   
                            #invalid loading
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Loading at : \n"+line)#f_call_fixer

                    # load ModuleName 
                    elif 'load' in line:
                                                    
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

                                loaded_modules[module_indx] = [TmpLsMdNames, None, '@']
                                module_indx += 1
                            
                            # case load modName
                            else:
                                for md in TmpLsMdNames:
                                    if self.__checkValidName(md) == False:
                                        print("[LINE:"+str(line_nbr+1)+"] - Invalid Module Name "+md+" ?")
                                        exit(0)

                                loaded_modules[module_indx] = [TmpLsMdNames, self.abs_file_path, '_']
                                module_indx += 1
                        else:
                            print("[LINE:"+str(line_nbr+1)+"] - Invalid Loading at : \n"+line)#f_call_fixer
                    
                    # User Not Allowed to Load anymore , since he started coding
                    # Which means basically once some codes other than loading shows up , that means no loading possible
                    # So the loading always must be at top !
                    # We will use a predefined method after to load the module temporarly and deestroy it at next line.
                    #
                    # This else will Set the can_load to False so the next lines are only for code that is not for loading
                    else:
                        can_load = False
                        self.__dico['modules'] = loaded_modules

                # this else will handle everything else
                #       L E T S   G 0 !
                else:
                    EntryPoint = None # we will store the line
                    noneSpacedLine = line.strip().replace(' ', '').replace('\t', '').replace('\n', '')

                    # Since we are handling .als :
                    # - There should be a $space { } <-- entry point
                    # - No $Function Declaration inside $space()
                    # - No Planet / IPlanet or oop stuff

                    # 1 - Checking for $space {} and getting it's Line .
                    #     |_ Keep Checking if its Repeated .
                    if '$space' in line and EntryPoint != None :
                        print("+ $space() Entry Point Already Defined at Line "+str(EntryPoint))
                        exit(0)
                    
                    elif '$space' in line and EntryPoint == None:
                        EntryPoint = line_nbr
                        # Line of entry
                        self.__dico['entry'] = EntryPoint
                    
                    # inside $space()
                    elif EntryPoint != None:
                        pass

                    else:
                        #global // outside of $space
                        # Functions Are possible
                        # variables are possible
                        pass

                    
                    pass
            
            

            #-------------------------------#
            #       TEST OUTPUT FILE        #
            #        DELETE AFTER           #
            #_______________________________#

            print("+ Done !")
            print(__import__('json').dumps(self.__dico , indent=4))
        
        else:
            print("+ Not Valid .als File !")
            exit(0)

    def __DotWals(self):
        pass

    def __DotMals(self):
        pass

    # TO DO ##########
    #
    #   - Loads that uses '...'  , quotes must be handled
    #  
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