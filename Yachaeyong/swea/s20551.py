# 20551

def solve():
    N = len(candy)
    cnt = 0
    for i in range(N - 1, 0, -1):
        if candy[i] == 1:
            return -1
        if candy[i - 1] >= candy[i]:
            while candy[i-1] >= candy[i]:
                candy[i-1] -= 1
                cnt += 1
    return cnt

T = int(input())
for tc in range(1, T + 1):
    candy = list(map(int, input().split()))
    print(f'#{tc} {solve()}')
