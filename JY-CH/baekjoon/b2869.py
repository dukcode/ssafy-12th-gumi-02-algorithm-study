# 달팽이는 올라가고 싶다

# 막대를 올라간다
# 올라가고 내려가기를 반복
# 근데 도착하면 거기서 끝
# while로 조건 달성시 끝내기? -> 터짐
# 그냥 몫에서 1더하면 되나?


import sys
input = sys.stdin.readline


a, b, v = map(int, input().split())


daily = a - b
real = v - a

day = 1 + (real // daily)
if real % daily != 0:
    day += 1


print(day)