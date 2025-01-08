# 시각

N = int(input())

cnt = 0

for i in range(N+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1

    print(str(i) + str(j) + str(k))
print(cnt)

# 요새 왤케 멍청해졌지




