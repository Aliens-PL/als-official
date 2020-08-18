#__import__('sys').path.append('..') # Get rid of higher dir msg
from __c import Cfg
import ctypes , glob

LEXER_C_SH_LIB_PATH = '../_clibs_/lib__lexer.so'

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
            lPath =  glob.glob(LEXER_C_SH_LIB_PATH)[0]

            assert lPath != None , 14 #f_call_fixer
            assert lPath != "" , 14 #f_call_fixer
            
            lexLib = ctypes.CDLL(lPath)

            assert lexLib != None , 15 #f_call_fixer

            lexLib.Lexer.restype = ctypes.c_void_p
            
            # PROTO => (const char * cfg , const char * src )
            #lexLib.Lexer.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

            lexLib.Lexer(b"SAAD CONFIG" , b"SAAD SRC ALS CODE")

        except Exception as ex:
            raise ex
            exit(-1)#f_call_fixer
        
    
