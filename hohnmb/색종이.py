w_paper = [[0]*100 for _ in range(100)]
paper_num = int(input())
cnt = 0
for _ in range(paper_num):
    a, b = map(int,input().split())
    for i in range(a,10+a):
        for j in range(b,10+b):
            w_paper[i][j] = 1

for i in range(100):
    for j in range(100):
        if w_paper[i][j] == 1:
            cnt += 1

print(cnt)