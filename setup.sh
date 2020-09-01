#!/bin/bash

echo '
          _      _____ ______ _   _  _____            _____  _      
    /\   | |    |_   _|  ____| \ | |/ ____|          |  __ \| |     
   /  \  | |      | | | |__  |  \| | (___    ______  | |__) | |     
  / /\ \ | |      | | |  __| | . ` |\___ \  |______| |  ___/| |      
 / ____ \| |____ _| |_| |____| |\  |____) |          | |    | |____ 
/_/    \_\______|_____|______|_| \_|_____/           |_|    |______| v0.1

+ Github    : https://github.com/AliensPL/als-official
+ Made by   : @samoray1998 , @AdilMERZ , @x544D , @Mahmoud_Omrani
+ Note      : This is still not even fully functional , the main idea of this is,
              To Provide Our Idea , we Had litteraly no time to finish all this ,
              Since we only worked as 3 of us , But we will keep pushing it to the top :D .

+ Usage : als help

'

scr_dir=$(dirname "$(readlink -f "$BASH_SOURCE")")/tools/


chmod 777 $scr_dir'als.py'
chmod 777 ~/.bashrc

echo 'PATH=$PATH:'$scr_dir >> ~/.bashrc
echo alias als='als.py' >> ~/.bashrc

exec bash

echo '+ Done !'
