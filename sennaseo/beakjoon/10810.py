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

# 리스트 안에 있는 요소를 꺼내는 방법을 아는데 중첩 for문을 써야하는 줄 알고
# ball리스트 요소를 뽑으려고 위에 for문과 연결되는 중첩 for문만 돌렸다.
# 그러나 ball 리스트는 완성되었기 때문에 굳이 중첩 for문 돌릴 필요 없이
# 바깥에 for문을 돌려서 ball 리스트 요소만 빼내면 됐었다.