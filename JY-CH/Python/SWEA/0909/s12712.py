# 파리퇴치 3

# 상 하 좌 우
dy =[-1, 1, 0, 0]
dx =[0, 0, -1, 1]
# 좌상 우상 우하 좌하
dy1 = [-1, -1, 1, 1]
dx1 = [-1, 1, 1, -1]



def max_kill(length, power, area):
    final_kill = 0
    for y in range(length):
        for x in range(length):
            kill_score = kill_score2 = area[y][x]
            for way in range(4):
                for p in range(1, power):
                    ny = y + dy[way]*p
                    nx = x + dx[way]*p
                    ny1 = y + dy1[way]*p
                    nx1 = x + dx1[way]*p

                    if 0 <= ny < length and 0 <= nx < length:
                        kill_score += area[ny][nx]
                    if 0 <= ny1 < length and 0 <= nx1 < length:
                        kill_score2 += area[ny1][nx1]

                if final_kill < kill_score:
                    final_kill = kill_score

                if final_kill < kill_score2:
                    final_kill = kill_score2

    return final_kill



for tc in range(int(input())):
    n, m = map(int, input().split())
    zone = [list(map(int, input().split())) for _ in range(n)]
    result = max_kill(n, m, zone)
    print(f'#{tc+1} {result}')
