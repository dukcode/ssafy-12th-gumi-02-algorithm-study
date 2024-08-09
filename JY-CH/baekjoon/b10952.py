# A + B - 5



import sys

# t = 0
# for tc in range(t):
#     t += 1

# for tc in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     if a == 0 or b == 0:
#         continue
#     print(a + b)


# t 지정 못해줘서 못품

# 15분 초과



while 1:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 or b == 0:
        break
    print(a + b)




# t 지정을 못하면 while문을 돌리자..
# a,b가 조건문안에 들어있어 범위 지정이 불가능하다
# 그럴땐 while문에 1을 넣어 True가 되게끔 만든다