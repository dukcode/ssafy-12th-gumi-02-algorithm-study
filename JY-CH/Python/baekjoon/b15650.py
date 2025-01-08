# n 과 m (2)
import sys
input = sys.stdin.readline

def find_all(n, m, data, start):
    
    # 길이 m이면 출력한다다
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(start, n + 1):
        # 집어 넣고
        data.append(i)
        # 수 1개 올리고 돌린다
        find_all(n, m, data, i + 1)
        # 그리고 끝났으면 빼고
        data.pop()


n, m = map(int, input().split())
start = 1
data = []
find_all(n, m, data, start)