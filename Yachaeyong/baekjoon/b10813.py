# 10813_공 바꾸기

N, M = map(int, input().split())
box = []

for n in range(1, N+1): #각 박스 번호에 맞는 공 생성
    box.append(n)

for x in range(1, M+1):
    i, j = map(int, input().split())
    temp = box[i-1] #임시 박스에 i번 박스 공 넣고
    box[i-1]=box[j-1]# i번 박스에 j번 박스 공 넣고
    box[j-1]= temp #j번 박스에 임시 박스에 있는 i번 박스 공 넣기

for y in range(N):
    print(box[y], end=' ')