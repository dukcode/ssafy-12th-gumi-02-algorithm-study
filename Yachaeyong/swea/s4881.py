def col_sum(r, cur_sum=0):
    global min_sum

    # 행 다 돌았으면 최소값과 비교하고 좌표 저장
    if r == N:
        # if min_sum > cur_sum:
        min_sum = cur_sum
        return

    for c in range(N):
        # 해당 열을 선택 안 했고 이때까지 합에 현재 요소 더해도 최소값 보다 작으면
        if not check_col[c] and cur_sum + arr[r][c] < min_sum:
            # 해당 값을 누적 합
            cur_sum += arr[r][c]
            # 해당 열 체크 표시
            check_col[c] = 1

            # 다음 행으로 넘어가서 반복
            col_sum(r + 1, cur_sum)

            cur_sum -= arr[r][c]
            check_col[c] = 0


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    check_col = [0] * N
    min_sum = 0xFFFF
    col_sum(0)
    print(f'#{tc} {min_sum}')