from _lexer_.lexer import Lexer
from _parser_.parser import Parser


class CoreEngine(object):
    
    def __init__(self, _tmp_f , fpath):
        lex = Lexer(_tmp_f , fpath)
        self.__lexDict = lex.GetLexDict()
        del lex
        par = Parser(self.__lexDict)
    
    





if __name__ == "__main__":
    argz = __import__('sys').argv
    if argz.__len__() >= 2 :
        CoreEngine(argz[1] , '')
    else:
        CoreEngine('file.als' , '')