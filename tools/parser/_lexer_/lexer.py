#__import__('sys').path.append('..') # Get rid of higher dir msg
from __c import Cfg


#---TO DO--------------------------------------------------------------------------------#

#- Replace f_call_fixer => Call bin->fixer/updater to fix the last exception loged/cached

#----------------------------------------------------------------------------------------#

class Lexer(object):

    def __init__(self , abs_file_path):
        print("+ Starting Lexer ")
        self.maped_cfg_instance = Cfg()
        self.maped_cfg_value    = self.maped_cfg_instance.get_cfg()
        self.maped_cfg_len = self.maped_cfg_value.__len__()

        #f_call_fixer
        assert self.maped_cfg_len > 0 , 13

        try:
            for line in self.maped_cfg_value:
<<<<<<< HEAD
                print(str(line))
=======
                print(line)
                
>>>>>>> f95f07b20662781f5008d467df8ad2bd87352934

        except Exception:
            print("Excep happend !") 
            exit(-1)#f_call_fixer
        
    
