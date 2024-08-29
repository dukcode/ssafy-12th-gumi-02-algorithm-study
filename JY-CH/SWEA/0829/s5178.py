# 노드의 합

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    data = [0] * (N+1)
    for _ in range(M):
        A, B = map(int, input().split())
        data[A] = B


    for i in range(N, 0, -1):
        if data[i] == 0:
            if i * 2 + 1 > N:
                data[i] = data[i*2]

            else:
                data[i] = data[i*2] + data[(i*2)+1]

    print(f'#{tc} {data[L]}')