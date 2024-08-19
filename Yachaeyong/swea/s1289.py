# 1289 원재의 메모리 복구하기

T = int(input())
for tc in range(1, T + 1):
    target = list(map(int, input().strip()))
    N = len(target)
    memory = [0] * N

    cnt = 0
    for i in range(N):
        if target[i] == memory[i]:
            continue
        else:
            cnt += 1
            for j in range(i, N):
                if not memory[j]:
                    memory[j] = 1
                else:
                    memory[j] = 0
            if target == memory:
                break

    print(f'#{tc} {cnt}')
