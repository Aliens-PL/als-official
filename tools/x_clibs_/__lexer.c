#include <stdio.h>
#include "string.h"
#include <stdlib.h>
#include "__lexer.h"


extern const char ** u_case(const char * _f_)
{
    if (_f_[0] != '_') return (char *)U_CASE_INVALID_FLAG;

    // _ALS_MODULE
    // _ALS_CONDITION
    //  _ALS_OPERATION
    // _ALS_LOOP
    // _ALS_KEYWORD
    // _ALS_PREFS_F
    // _ALS_PREFS_C

    if      (_f_ == ALS_CONDITION)      return _ALS_CONDITION;
    else if (_f_ == ALS_MODULE)         return _ALS_MODULE;
    else if (_f_ == ALS_OPERATION)      return _ALS_OPERATION;
    else if (_f_ == ALS_LOOP)           return _ALS_LOOP;
    else if (_f_ == ALS_KEYWORD)        return _ALS_KEYWORD;
    else if (_f_ == ALS_PREFS_F)        return _ALS_PREFS_F;
    else if (_f_ == ALS_PREFS_C)        return _ALS_PREFS_C;

    else return (char *)U_CASE_404_FLAG;

    //incase
    return NP(char **);
}



extern const unsigned char * p_case(const char * _f_)
{
    if (_f_[0] != '.') return P_CASE_INVALID_FLAG;

    if (_f_ == ALS_SYMBOLE_1) return _ALS_SYMBOLE_1;
    else if (_f_ == ALS_SYMBOLE_2) return _ALS_SYMBOLE_2;
    else return P_CASE_404_FLAG;

    // incase
    return NP(char *);
}