gcc -c -Wall -Werror -fpic __lexer.c
gcc -shared -o lib__lexer.so __lexer.o
