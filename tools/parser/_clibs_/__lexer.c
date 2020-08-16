#include <stdio.h>
#define np (void *)0

void * Lexer(const char * cfg , const char * src )
{
    while (*cfg != '\0')
    {
        puts(cfg);
        cfg++;
    }
    
    printf("\n\n");

    while (*src != '\0')
    {
        puts(src);
        src++;
    }

    return np;
}