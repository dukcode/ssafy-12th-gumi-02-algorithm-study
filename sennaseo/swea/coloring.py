T = int(input())

for tc in range(1, T + 1):

    # 10 * 10 2차원 리스트 생성
    arr = [[0] * 10 for _ in range(10)]
    N = int(input())

    # 칠할 영역의 범위와 색을 알려주는 입력을 받고 그 영역내를 순회합니다.
    for _ in range(N):
        x1, y1, x2, y2, color = map(int, input().split())

        for y in range(y1, y2 + 1):
            for x in range(x1, x2 + 1):
                # arr[y][x] += color
                # 영역 arr[y][x] == 0이라면 color값(빨강 1, 파랑 2)을 입력하고,
                # 영역 arr[y][x]에 값이 있고 arr[y][x] != color이라면 3(보라)를 입력합니다.
                if arr[y][x]:
                    if arr[y][x] != color:
                        arr[y][x] = 3
                else:
                    arr[y][x] = color

    # arr 2차원 리스트를 순회하며 '3'의 개수를 셉니다.
    cnt = 0
    for y in range(10):
        for x in range(10):
            if arr[y][x] == 3:
                cnt += 1

    print(f'#{tc} {cnt}')
