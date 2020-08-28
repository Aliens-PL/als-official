#!/bin/bash

echo "
+----------------- ALS-WELCOME------------------+
-	github : Aliens-PL/als-official
+-----------------------------------------------+

+ Usage : als [-help] [createproject] [run] [update] [remove]	
+ NOTE : this project is still in alpha test, so we expect a lot of bugs reports from you :) .

"

scr_dir=$(dirname "$(readlink -f "$BASH_SOURCE")")/tools/parser/


chmod 777 $scr_dir'als.py'
chmod 777 ~/.bashrc

echo 'PATH=$PATH:'$scr_dir >> ~/.bashrc
echo alias als='als.py' >> ~/.bashrc

exec bash

echo '+ Done !'
