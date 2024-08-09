# 돌 뒤집기

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(1, M+1):
        i, j = map(int, input().split())
        # i부터 i+j까지
        for k in range(i - 1, i - 1 + j):
            # 인덱스가 배열 길이 초과 방지
            if k < N:
                # arr[i-1] 값으로 바꾸기
                arr[k] = arr[i - 1]

    print(f'#{tc}', end=' ')
    print(*arr)
