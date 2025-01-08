#안테나
import sys
input = sys.stdin.readline

house = int(input())

pos = list(map(int, input().split()))

pos = sorted(pos)

# 시간 초과
# solve = 99999999
# answer = 999999
# for idx in range(1, pos[-1]):
#     result = 0
#     for house_pos in pos:
#         result += abs(house_pos - idx)
    
#     if solve > result:
#         solve = result
#         answer = idx
#     else:
#         pass

# 무슨 짓을해도 중간값에서 찍어야 최소가 찍힘
# 짝수의 경우 같 .5가 찍히는데
# 같은 값의 경우 작은걸 뽑아야하므로 1을 뺀다
answer = pos[(house - 1)//2]  

print(answer)
        