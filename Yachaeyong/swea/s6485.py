T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    stops = [0] * 5001
    for i in range(N):
        A, B = map(int, input().split())
        for j in range(A, B+1):
            stops[j] += 1
    P = int(input())

    stop_num = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for num in stop_num:
        print(stops[num], end=' ')
    print()