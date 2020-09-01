import ctypes , glob , os


libf = glob.glob('C:\\Users\\544D\\Desktop\\J A M\\als-official\\tools\\parser\\_clibs_\\lib__lexer.so')[0]

if libf:
    print("+ Found "+str(libf))
    lib = ctypes.CDLL(libf)

    if lib :
        print("+ Loaded "+str(libf))
        lib.Lexer.restype = None
        lib.Lexer.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

        lib.Lexer(b'SAAD IS TESTING', b'This is not a valid import')
