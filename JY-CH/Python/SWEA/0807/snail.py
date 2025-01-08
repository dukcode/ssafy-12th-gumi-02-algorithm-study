
# 달~팽이!

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    # 우 하 좌 상
    mr = [0, 1, 0, -1]
    mc = [1, 0, -1, 0]


    # 배열의 시작점에서 갈거니까 0으로 잡고 방향을 변수명으로 0할당
    # 숫자 넣으면서 갈거니까 1할당
    # 숫자의 최대치까지 갈거니까 받아온 n을 제곱으로 조건
    # 한칸 지날때마다 num += 1 해야됨
    # 문제는 벽에 밖을때, 숫자가 있을때 방향을 돌리게끔 해야됨.
    # 드갖으ㅏㅏㅏ
    r, c = 0, 0
    direction = 0
    num = 1
    while num <= n*n:
        arr[r][c] = num
        num += 1
        nr = r + mr[direction]
        nc = c + mc[direction]
        if nr < 0 or nr >= n or nc < 0 or nc >= n or arr[nr][nc] != 0:
            direction = ((direction + 1) % 4)
        r += mr[direction]
        c += mc[direction]

    print(*arr)
