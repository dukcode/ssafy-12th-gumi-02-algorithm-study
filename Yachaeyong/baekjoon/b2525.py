# A, B = map(int, input().split())
# C = int(input())

# if A > 0 and C < 60:
#     if B+C < 60:
#         B += C
#         print(A, B)
#     elif A == 23 and B+C > 60:
#         A = 0
#         B = B+C-60
#         print(A, B)
#     else:# B+C>60:
#         A+=1
#         B=B+C-60
#         print(A, B)
# elif A > 0 and C > 60:
#     if A < 6 and B+C < 1060:
#         A = A + ((B+C)//60)
#         B = (B+C) % 60
#         print(A, B)
#     elif A > 6 and B+C < 1060:

# 조건에 너무 집착해서 코드 더럽고 빠지는 조건도 발생

A, B = map(int, input().split())
C = int(input())

# 현재 시각에 요리 시간을 더한 분 단위의 시각 계산
B += C

# 시와 분으로 나누어 다시 계산
if B >= 60:
    A += B // 60
    B = B % 60

# 시가 24시간을 초과할 경우 24로 나눈 나머지로 변환
if A >= 24:
    A = A % 24

# 출력
print(A, B)