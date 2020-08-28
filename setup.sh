#!/bin/bash

scr_dir=$(dirname "$(readlink -f "$BASH_SOURCE")")/tools/parser/


chmod 777 $scr_dir'als.py'
chmod 777 ~/.bashrc

echo 'PATH=$PATH:'$scr_dir >> ~/.bashrc
echo alias als='als.py' >> ~/.bashrc

exec bash

echo '+ Done !'
