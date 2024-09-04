# 최소 합

def solve(y=0, value=0):
    # 최소합 호출
    global min_sum

    # 행이 n개랑 같으면
    # 현재 값을 최소합에 저장
    if y == n:
        min_sum = value
        return

    for i in range(n):
    # 같은 열은 사용하지 않았으며 저장한 값이 현재 최소값 보다 작으면
        if not check[i] and value + arr[y][i] < min_sum:
            # 열 체크한 다음
            check[i] = True
            # 바로 다시 함수에 넣고 돌리기
            solve(y + 1, value + arr[y][i])
            check[i] = False



for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    min_sum = 9 * n
    check = [False] * n

    solve()

    print(f'#{tc+1} {min_sum}')

