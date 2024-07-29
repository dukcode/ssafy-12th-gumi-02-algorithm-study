# 첫째줄에 N과 M이 주어진다
# 둘째줄부터 M개의 줄에 걸쳐서 공을 넣는 방법이 주어진다
N, M = map(int, input().split())
ball = [0]*N
for x in range(1, M+1):
    a, b, c = map(int,input().split())
    for i in range(a-1, b):
        ball[i] = c
for x in ball:
    print(x, end=' ')