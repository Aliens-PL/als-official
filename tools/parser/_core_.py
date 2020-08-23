from _lexer_.lexer import Lexer

class CoreEngine(object):
    
    def __init__(self, _tmp_f , fpath):
        Lexer(_tmp_f , fpath)



if __name__ == "__main__":
    CoreEngine('file.als' , '')