# 문자열 반복

T = int(input())

for t in range(T):
    R, S = input().split()

    for i in S:
        print(int(R) * i, end='') #개행문자제거
    print() #줄 바꿈용