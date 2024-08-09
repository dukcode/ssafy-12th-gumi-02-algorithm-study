# 그대로 출력하기

import sys

words = sys.stdin.readlines() 
#readlines : 여러 입력 한 번에 받아 list로 반환
#아직 sts.stdin은 어색함
for word in words:
    print(word.rstrip())
    #rstrip으로 개행문자 제거