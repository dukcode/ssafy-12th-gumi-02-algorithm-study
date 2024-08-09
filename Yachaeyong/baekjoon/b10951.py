# A+B - 4
#두 정수 A와 B를 입력받은 다음, 입력이 끝날 때까지 A+B를 출력하는 프로그램을 작성

import sys
# 표준 입력으로부터 모든 입력을 읽어옴
input = sys.stdin.read

# 읽어온 입력을 줄 단위로 분리하여 리스트로 저장
data = input().strip().split('\n')

# 각 줄에 대해 처리
for line in data:
    A, B = map(int, line.split())
    print(A + B)

#입력 종료는 ctrl+Z로 한다;;