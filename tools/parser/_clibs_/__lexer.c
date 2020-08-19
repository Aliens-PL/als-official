#include "__lexer.h"
#include <stdio.h>
#include "string.h"

#define NP (void *)0


void * Lexer(const char * cfg , const char * src )
{
    //
    return NP;
}



void * check_loads(const char * line)
{
    /*
     *  Possible cases for loading :
     *  1- load ModuleName
     *  2- from 'http://....../file.als' load ModuleName
     *  3- from 'path_to_file/file.als' load ModuleName
     *  4- load @base
     *  5- from @base load @convert
    */
    
    // check if valid loading
    // Hardcoded indexes!
    if ((*strstr(line, *_ALS_MODULE[0]) | *strstr(line, *_ALS_MODULE[1]) | *strstr(line, *_ALS_MODULE[2])) == NULL)
    {
        
    }
    

    size_t _len_ = strlen(line);


    for (size_t i = 0; i < _len_ ; i++)
    {
        
    }
    
}