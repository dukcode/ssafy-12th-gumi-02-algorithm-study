# 삼성시의 버스 노선

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    counts = [0] * 5001


    for _ in range(N):
        A, B = map(int, input().split())
        for i in range(A, B+1):
            counts[i] += 1


    P = int(input())
    station = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for j in station:
        print(counts[j], end=' ')
    print()


