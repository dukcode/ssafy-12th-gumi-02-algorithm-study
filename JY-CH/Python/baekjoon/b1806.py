# 부분합

import sys
input = sys.stdin.readline

n, s = map(int, input().split())

data = list(map(int, input().split()))

# 이진탐색을 시작부터 못하나 흠
def find_part_sum(n, s, data):
    start, end = 0, 0
    cur_sum = 0
    min_length = 99999999

    while end < n:
        # 계속 누적합을 시킨다.
        cur_sum += data[end]
        end += 1

        # 근데 이게 넘으면 빼야됨
        while cur_sum >= s:
            # 결국 다 추적해야됨
            # 같은 값을 달아서 멈추면 더 작은값을 못찾음.
            # 최소거리 갱신하고
            min_length = min(min_length, end - start)
            # 누적합에서 현재 위치값을 뺀다
            cur_sum -= data[start]
            # 그리고 시작점 옮겨야지
            start += 1
    
    # 내가 지정한 값보다 작으면 값이 변동 됬으니까
    if min_length != 99999999:
        return min_length
    else:
        return 0


# 이거 왜 됨????
print(find_part_sum(n, s, data))


