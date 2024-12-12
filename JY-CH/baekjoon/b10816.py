# 숫자 카드2
import sys
input = sys.stdin.readline

n = int(input())
data = list(map (int, input().split()))
m = int(input())
check = list(map (int, input().split()))

# 시간초과 풀이
# result = [0] * (m)
# for i in range(len(check)):
#     for number in data:
#         if number == check[i]:
#             result[i] += 1
#     print(result[i], end=" ")


# 중첩 반복문 m * n => 시간초과 발생

count = {}
for number in data:
    if number in count:
        count[number] += 1
    else:
        count[number] = 1

result = []
for number in check:
    print(count[number] if number in count else 0, end=" ")