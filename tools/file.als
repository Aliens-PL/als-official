# Hello

from https://www.epa.gov/robots.txt load Saad
from @base load         @convert,      @C , @DSDS_ , @K


load SaadModule
load @base
from ../../this load ThisPlanetA

using @convert



$SayHi _name _prenom 
{
    if(_name == "saad"){
        _name = "SAAD"
    }
    :(_name == "adil")
    {
        _name = "ADIL" 
    }:(_name == "jamal")
    {
        _name = "JAMAL"
    }
    :{
        _name = "UNKNOWN"
    }

    @loop(1, 5) as x
    {
        _prenom += $str(x)
    }

    # shoud print _name + _prenom12345
    return _name + _prenom
}

$space  ( ) 
{
    _$LNAME = "AMRNAI"
    _$RNAME = "SAAD"
    planets = $Sayhi(_$LNAME , _$RNAME)
    $show(planets)
}

# sas als

# Sa 

