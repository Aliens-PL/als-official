from _lexer_.lexer import Lexer
from _parser_.parser import Parser


class CoreEngine(object):
    
    def __init__(self, _tmp_f , fpath):
        lex = Lexer(_tmp_f , fpath)
        self.__lexDict = lex.GetLexDict()
        del lex
        open(__import__('os').path.join(fpath, 'lexer_output.json') , 'w+').write(__import__('json').dumps( self.__lexDict , indent = 4))
        par = Parser(self.__lexDict)
    
    