#!/bin/bash

echo '############# Thanks for using ALS Lang #############\n\t- Made By 0x544D, ADIL, JAMAL\n\tgithub : https://github.com/Aliens-PL/als-official\n#######################################################\n\n'

scr_dir=$(dirname "$(readlink -f "$BASH_SOURCE")")/tools/parser/


chmod 777 $scr_dir'als.py'
chmod 777 ~/.bashrc

echo 'PATH=$PATH:'$scr_dir >> ~/.bashrc
echo alias als='als.py' >> ~/.bashrc

exec bash

echo '+ Done !'
