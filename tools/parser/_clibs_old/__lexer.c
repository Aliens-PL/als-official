#include <stdio.h>
#include "string.h"
#include <stdlib.h>
#include "__lexer.h"


void Lexer(const char * cfg , const char * src )
{

	printf("+ Len = %s  !\n", src);

	check_loads(src);

}

void check_loads(const char * line)
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
    if ((*strstr(line, _ALS_MODULE[0]) | *strstr(line, _ALS_MODULE[1]) | *strstr(line, _ALS_MODULE[2])))
    {
	printf("+ Valid load !\n");        
    }
    else printf("- Not Valid load !\n");       
} 
