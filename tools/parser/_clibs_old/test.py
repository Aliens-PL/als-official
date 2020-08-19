import ctypes , glob , os


libf = glob.glob('/home/saad/Desktop/_clibs_/*.so')[0]

if libf:
    print("+ Found "+str(libf))
    lib = ctypes.CDLL(libf)

    if lib :
        print("+ Loaded "+str(libf))
        lib.Lexer.restype = None
        lib.Lexer.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

        lib.Lexer(b'SAAD IS TESTING', b'This is not a valid import')
