# 사~다~리~잉

def solve(r, c):

    way = 0
    mr = [1, 0, 0]
    mc = [0, -1, 1]
    while r < 99:
        r += mr[way]
        c += mc[way]

        if way == 0:
            if c > 0 and arr[r][c-1] == 1:
                way = 1
            elif c < 99 and arr[r][c+1] == 1:
                way = 2
        else:
            if r < 99 and arr[r+1][c] == 1:
                way = 0

    if arr[r][c] == 2:
        return True
    else:
        return False

for _ in range(10):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

    for i in range(100):
        if arr[0][i] == 1:
            if solve(0, i) == True:
                print(f'#{tc} {i}')
                break


# if문 조건 설정만 잘하면 되는데
# 그걸 못해서 못했던 문제..
#