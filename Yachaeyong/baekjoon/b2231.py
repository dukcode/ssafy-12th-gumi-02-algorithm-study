# 분해합

N = int(input())

for i in range(N):
    # 자릿수 더하는 방법 중 하나
    ans = i + sum(map(int, str(i)))
    if ans == N:
        print(i)
        break
else:
    print(0)