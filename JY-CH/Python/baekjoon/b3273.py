# 두수의 합

import sys
input = sys.stdin.readline


n = int(input())

data = list(map(int, input().split()))

data.sort()

x = int(input())

# 투 포인터 재밌당
def find_sum(data):
    start, end = 0, len(data) - 1
    target = x
    current_sum = 0
    cnt = 0

    while start < end:
        current_sum = data[start] + data[end]

        if current_sum == target:
            cnt += 1
            start += 1
            end -= 1
        elif current_sum > target:
            end -= 1
        else:
            start += 1


    return cnt

print(find_sum(data))

