def find_path(pic, y, x, dir=None):
    if dir:
        get_lenth(pic, y, x, dir)
    else:
        if pic[y][x]:
            directions = ((1, 0), (0, 1))
            longest = 0
            for direction in directions:
                longest = max(longest, get_lenth(pic, y, x, direction))
            return longest
        else:
            return 0


def get_lenth(pic, y, x, dir):
    nextY = y + dir[0]
    nextX = x + dir[1]
    if nextY < len(pic) and nextX < len(pic[y]) and pic[nextY][nextX]:
        return pic[y][x] + get_lenth(pic, nextY, nextX, dir)
    else:
        return 0


for tc in range(int(input())):
    h, w = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(h)]
    ans = 0
    for y in range(h):
        for x in range(w):
            ans = max(ans, pic[y][x] + find_path(pic, y, x))
    print(f'#{tc + 1} {ans}')
