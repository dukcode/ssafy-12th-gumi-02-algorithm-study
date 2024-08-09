for tc in range(1, 10 + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    board = list(zip(*board))

    cnt = 0

    # 1은 오른쪽으로 향함
    # 2는 왼쪽으로 향함
    for col in board:
        is_n_before = False
        for mag in col:
            if mag == 1:
                is_n_before = True
                continue
            if mag == 2:
                if is_n_before:
                    cnt += 1
                    is_n_before = False

    print(f"#{tc} {cnt}")
