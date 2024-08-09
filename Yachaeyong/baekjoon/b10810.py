# 10810 공 넣기

N, M = map(int, input().split())

box = [0] * N #빈 박스 생성

for _ in range(M):
    i, j, k = map(int, input().split())
    for x in range(i, j+1): #i부터 j번 박스까지
        box[x-1] = k #박스 번호는 1부터 시작인데 리스트 인덱스는 0부터 시작이므로 -1해줌

for y in range(N):
    print(box[y], end=' ')