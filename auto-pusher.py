# 0 X 5 4 4 D # x #

from time import sleep
from os import system


_PUSH_EACH  = 3600 # 1h
_PUSH_ADD   = '.'
_PUSH_BRNCH = 'saad'


while True:    
    system("git add "+_PUSH_ADD)
    system("git commit -m 'From_AP'")
    system("git push origin "+_PUSH_BRANCH)

    sleep(_PUSH_EACH)
