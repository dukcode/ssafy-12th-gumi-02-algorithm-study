# 배열 최소합

def solve(idx, my_sum, n):
    global min_sum
    if idx == n:
        if min_sum > my_sum:
            min_sum = my_sum
        return
 
    for i in range(n):
        if not check_col[i] and my_sum < min_sum:  
            check_col[i] = 1  
            solve(idx + 1, my_sum + arr[idx][i], n)
            check_col[i] = 0  
 
 
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_sum = 10 * (N**2)
    check_col = [0] * N
    solve(0, 0, N)
 
    print(f'#{tc} {min_sum}')