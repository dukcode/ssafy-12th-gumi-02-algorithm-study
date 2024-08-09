# 사~다~리~잉

t = int(input())

for tc in range(1, t+1):
    arr = [[list(map(int, input().split()))] for _ in range(100)]

    # 어차피 탈게 사다리면 위로 갈 필요가 없는데
    # 빼보자!
    mr = [0, 1, 0]
    mc = [1, 0, -1]
    way = 0
    row, col = 0, 0

    for row in range(100):
        if arr[row][col] == 0:
            continue
        else:
            row += mr[way]
            col += mc[way]

