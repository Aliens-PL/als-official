#__import__('sys').path.append('..') # Get rid of higher dir msg
from __c import Cfg

class Lexer(object):

    def __init__(self , abs_file_path):
        print("+ Starting Lexer ")
        self.maped_cfg_instance = Cfg()
        self.maped_cfg_value    = self.maped_cfg_instance.get_cfg()
        self.maped_cfg_len = self.maped_cfg_value.__len__()

        #assert self.maped_cfg_len > 0 , "[ERR] cfg File Returned Null .. !"

        try:
            for line in self.maped_cfg_value:
                print(str(line))

        except Exception as ex:
            print(ex)
        
    
