n = int(input())
arr_a = sorted(list(map(int, input().split())), reverse=True)
arr_b = sorted(list(map(int, input().split())))

ans = 0
for i in range(n):
    ans += arr_a[i] * arr_b[i]

print(ans)
