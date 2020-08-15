# 0 X 5 4 4 D # x #

from time import sleep
from os import system


_PUSH_EACH  = 3600 # 1h
_PUSH_ADD   = '.'
_PUSH_BRNCH = 'saad'

cnt = 0

while True:    
    system("git add "+_PUSH_ADD)
    system("git commit -m 'From_AP'")
    system("git push origin "+_PUSH_BRNCH)
    cnt += 1
    print("\n----------------[ PUSH NBR "+str(cnt)+" ]----------------\n")
    sleep(_PUSH_EACH)

