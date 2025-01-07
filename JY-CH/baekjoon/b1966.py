# 프린터 큐

# 프린터 큐

# 입력
import sys
input = sys.stdin.readline

# 큐 불러오기
from collections import deque

def find_doc():

    # 큐에 담았음.

    queue = deque()
    for idx in range(len(arr)):
        queue.append(arr[idx])
    
    cnt = 0
    # 큐
    while queue:
        # 큐 빼고
        num = queue.popleft()
        
        # 최대 큐 확인
        max_queue = max(queue, default=(0, -1))[0]
        # 작으면 다시 넣고
        if num[0] < max_queue:
            queue.append(num)
        else:
            # 같거나 작으면 카운트 += 1
            # m이랑 같으면 종료
            cnt += 1
            if num[1] == m:
                return cnt
    

# tc 3개
tc = int(input())

# n개 = len(arr)
# m = 몇번째로 인쇄됬는지 궁금한 문서의 현 위치
# 순번은 0번째 시작
for _ in range(tc):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    # arr[i]를 tuple 형태로 취해서 idx와 함께 묶는다.
    for i in range(len(arr)):
        arr[i] = (arr[i], i)


    print(find_doc())