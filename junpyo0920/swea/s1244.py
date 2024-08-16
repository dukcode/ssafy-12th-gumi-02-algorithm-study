def dfs(n=0):
    if n == int(count):
        global ans
        ans = max(ans, int("".join(num_list)))
        return
    for i in range(N - 1):
        for j in range(i + 1, N):
            num_list[i], num_list[j] = num_list[j], num_list[i]
            if (n, int("".join(num_list))) not in v:
                dfs(n + 1)
                v.add((n, int("".join(num_list))))
            num_list[j], num_list[i] = num_list[i], num_list[j]


for tc in range(int(input())):
    num, count = input().split()
    num_list = list(num)
    N = len(num_list)
    v = set()
    ans = 0
    dfs()
    print(f'#{tc+1} {ans}')