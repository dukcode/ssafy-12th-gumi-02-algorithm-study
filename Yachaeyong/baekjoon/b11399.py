N = int(input())
P = list(map(int, input().split()))

P.sort()

ans = []
temp = 0
for i in range(len(P)):
    temp += P[i]
    ans.append(temp)

print(sum(ans))