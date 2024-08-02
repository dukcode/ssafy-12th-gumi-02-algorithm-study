N , k = map(int, input().split()) 

cnt = [[0] * 6 for _ in range(2)]
result = 0
for i in range(N):
    gender , grade  = map(int, input().split())
    cnt[gender][grade - 1] += 1

for i in cnt :
    for j in i:
        if j % k == 0:
            result += j // k
        else:
            result += (j // k) + 1
print(result)