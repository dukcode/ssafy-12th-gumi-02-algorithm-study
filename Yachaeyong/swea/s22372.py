'''
1
0 0 2 2
4
-1 -1
0 0
1 1
2 2
'''

T = int(input())
for tc in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())
    N = int(input())

    cnt1 = cnt2 = cnt3 = 0

    for _ in range(N):
        x, y = map(int, input().split())
        # 점이 완전히 직사각형 내부에 있는 경우
        if x1 < x < x2 and y1 < y < y2:
            cnt1 += 1
        # 점이 직사각형의 네 변 중 적어도 하나의 위에 있는 경우
        elif (x1 <= x <= x2 and (y == y1 or y == y2)) or (y1 <= y <= y2 and (x == x1 or x == x2)):
            cnt2 += 1
        # 점이 완전히 직사각형 외부에 있는 경우
        else:
            cnt3 += 1

    print(f'#{tc} {cnt1} {cnt2} {cnt3}')
