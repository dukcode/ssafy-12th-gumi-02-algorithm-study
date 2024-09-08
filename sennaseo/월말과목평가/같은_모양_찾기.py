T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    pattern = [list(map(int,input().split())) for _ in range(3)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            pattern_cnt = 0
            for a in range(3):
                for b in range(3):
                    ia = i + a
                    jb = j + b
                    if 0 <= ia < N and 0 <= jb < N:
                        if arr[ia][jb] == pattern[a][b]:
                            pattern_cnt += 1
                    else:
                        break
            if pattern_cnt == 9:
                cnt += 1

    print(f'#{tc} {cnt}')