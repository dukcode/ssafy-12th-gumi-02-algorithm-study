# 부분 합

def solve(lst):

    max_value = 0
    min_value = 100000000

    for i in range(0, N - M + 1):
            if max_value < (sum(lst[i:i+M])):
                max_value = (sum(lst[i:i+M]))

            if min_value > (sum(lst[i:i+M])):
                min_value = (sum(lst[i:i+M]))

    return max_value - min_value

t = int(input())
for tc in range(1, t+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    result = solve(lst)
    print(f'#{tc} {result}')