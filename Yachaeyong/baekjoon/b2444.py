# 별 찍기 -7
# N번 줄 이후에는 역순으로 반복하는게 포인트.

N = int(input())

for i in range(1, N):
    print(' '*(N-i)+'*'*(2*i-1))

for i in range(N, 0, -1):
    print(' '*(N-i)+'*'*(2*i-1))