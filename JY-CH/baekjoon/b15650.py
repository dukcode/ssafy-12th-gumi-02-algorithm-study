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
        # 다시 함수에 넣어서 m 맞으면 출력 아니면 반복
        find_all(n, m, data, i + 1)
        # 그리고 끝났으면 빼고
        data.pop()


n, m = map(int, input().split())
start = 1
data = []
find_all(n, m, data, start)