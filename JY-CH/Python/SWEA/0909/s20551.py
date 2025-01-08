# 증가하는 사탕 수열

# 상자 a,b,c 3개
# 순증가하기를 원함 a < b < c
# a b c 최소 1
# 무조건 까는거 말고는 못함.
# 만족이 가능한지 판단, 된다면 몇개나 먹어야하는지.

# 안되는 걸 찾아야함.

# b c 는 1 이면 아웃.


def check(a, b, c):
    cnt = 0
    if b < 2 or c < 3:
        return -1

    if b >= c:
       cnt += b - (c - 1)
       b = c - 1

    if a >= b:
       cnt += a - (b - 1)
       a = b - 1

    return cnt


for tc in range(int(input())):
    a, b, c = map(int, input().split())
    result = check(a, b, c)
    print(f'#{tc+1} {result}')