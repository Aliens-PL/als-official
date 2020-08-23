#ifndef lexer_h__
#define lexer_h__


// ------------ COMFIGS ------------ //
#define MAX_POSSIBLE_MODULES_LOADS 0xB
#define NP(T) (T)0

#define P_CASE_INVALID_FLAG "ex::16"
#define U_CASE_INVALID_FLAG "ex::17"
#define P_CASE_404_FLAG     "ex::18"
#define U_CASE_404_FLAG     "ex::19"

// -----------    END    ----------- //


// BASIC PROGRAMMING

#define ALS_MODULE      "_A000"
#define ALS_CONDITION   "_A001"
#define ALS_OPERATION   "_A002"
#define ALS_LOOP        "_A003"
#define ALS_KEYWORD     "_A004"
#define ALS_PREFS_F     "_A005"
#define ALS_PREFS_C     "_A006"
#define ALS_SYMBOLE_1   ".A007"
#define ALS_SYMBOLE_2   ".A008"
#define ALS_FUNCTION    "_A009"
#define ALS_VARIABLE    "_A010"
#define ALS_F_PARAM     "_A011"

// O O P -

#define ALS_PLANET              "_B000"
#define ALS_CONSTRUCTOR         "_B001"

#define ALS_IPLANET             "_B002"
#define ALS_IPLANET_ABS_METHODE "_B003"

// ------------   TYPE DEFS   ------------ //

// typedef struct __LOADS
// {
//     char * path;
//     char * Modules[MAX_POSSIBLE_MODULES_LOADS];

// } LEX_LOADS;


// typedef struct __TOKEN
// {
//     int child_of;
//     char * type;
//     char * value;

// } LEX_TOKEN;


// typedef struct __LINE
// {
//     int number;
//     char * startType;
//     char * value;

// } LEX_LINE;

// ------------ CASES ------------ //

const char * _ALS_MODULE[] = 
{ 
    "from",
    "extern" // This for later on To import extern Classes / Functions (load them up and point on that object)
    "load",
};

const char * _ALS_CONDITION[] = 
{ 
    "?"     ,"??"   ,"if",
    ":"     ,"and"  ,"or",
    "=="    ,"&&"   ,"||",
    "in"
};

const char * _ALS_OPERATION[] = 
{ 
    "+"     ,"-"    ,"*",
    "/"     ,"%"    ,"=",
    ">>"    ,"<<"   ,"|",
    "^"     ,"&"    ,"~"
};

const char * _ALS_LOOP[] = 
{ 
    "while" ,"loop"
};

const char * _ALS_KEYWORD[] = 
{ 
    "ZM" ,      "null",     "space",
    "galaxy",   "planet",   "iplanet",
    "not",      "null",     "imported"
};

const char * _ALS_PREFS_F[] =
{
    // Coverting Funcs
    "tonumber",     "totext",       "tojson",
    "toxml",        "tobin",        "toascii",
    "todict",       "tolist",
    
    // Type Checking Funcs
    "istext",       "isdate",       "istime",
    "isnull",       "isequal",      "ismatch",

    // List basic Functions
    "add",          "insert",       "update",
    "remove",       "sort",         "reverse",
    "pick",         "find",         "size",
    "clear"

    // Math Functs -- this is better if we check only if loaded math module
    "sqrt",         "abs",          "pow",
    "fact",         "log",          "exp",
    "sin",          "cos",          "tan",
    "asin",         "acos",         "atan",
    "rand",         

    // date and time funcs
    "date",         "time",         "adddays",
    "diffdays",     "months",       "days",
    "years",        "hours",        "minutes",
    "seconds",

    // Strings Functions
    "lower",        "upper",        "split",
    "len",          "contains",     "inbetween",    
    "replace",      "slice",        "count"

    // Files Functions
    "f_extension",  "f_size",       "f_name",
    "f_delete",     "f_copy",       "f_move",
    "f_read",       "f_write",      "f_append",
    "f_loop_lines", "f_loop_bytes"

    // Global Use funcs
    "typeof",       "nameof",       "system",
    "als_test",

};

// constants starts with _$NAME (UPPERCASE)
const char * _ALS_PREFS_C[] = 
{ 
    "ALPHABETS_UPPER",      "ALPHABETS_LOWER",      "ASCII_TABLE",
    "WORD_SIZE",            "DWORD_SIZE",           "QWORD_SIZE",
    "NEW_LINE",             "ALS_VERSION",          "GITHUB_REPO",
    "SPONSOR_LINK",         "WEBSITE"
};

// Symboles that does not need opening-closing
const unsigned char _ALS_SYMBOLE_1[] = 
{
    0x40,   0x23,   0x21,   // @ # !
    0x2c,   0x5f,   0x24,   // , _ $
    0x2e,                   // .

};

// the opening is always at an index fardi
// the closing is always at an index zawji
const unsigned char _ALS_SYMBOLE_2[] = 
{
    0x7b,   0x7d,   // {}
    0x5b,   0x5d,   // []
    0x28,   0x29,   // ()
    0x27,   0x27,   // ''
    0x22,   0x22    // ""
};



/*
 *      ---- START ----
 *  SOME COOL PRESENTATIONS
 *  AND EXPLAINATIONS ...ETC
 *  SO THE USERS UNDERSTAND
 *      ---- END   ----
 */


// point_case
extern const unsigned char * p_case(const char *);
// underscore case
extern const char ** u_case(const char *);


#endif
