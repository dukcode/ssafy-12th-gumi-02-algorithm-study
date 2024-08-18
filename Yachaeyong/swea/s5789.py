# 5789 현주의 상자 바꾸기

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    boxes = [0] * N
    for i in range(1, Q + 1):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            boxes[j] = i

    print(f'#{tc}', *boxes)
