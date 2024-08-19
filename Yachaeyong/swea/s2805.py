# 2805 농작물 수확하기

for tc in range(1, int(input()) + 1):
    N = int(input())
    farm = [list(map(int, input().strip())) for _ in range(N)]
    price = 0
    # 증가
    for i in range(N // 2 + 1):
        for j in range(N // 2 - i, N // 2 + i + 1):
            price += farm[i][j]
    # 감소
    for i in range(N // 2 + 1, N):
        for j in range(i - N // 2, N - (i - N // 2)):
            price += farm[i][j]

    print(f'#{tc} {price}')
