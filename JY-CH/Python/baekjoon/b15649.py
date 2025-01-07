# n 과 m (1)
import sys
input = sys.stdin.readline

def find_all(n, m, data, visited):
    
    # 길이 m이면 출력한다다
    if len(data) == m:
        print(' '.join(map(str, data)))
        return

    for i in range(1, n + 1):
        # i 안나왔으면
        if not visited[i]:
            # 방문 체크  
            visited[i] = 1
            # 집어 넣고
            data.append(i)
            # 다시 함수에 넣어서 m 맞으면 출력 아니면 반복
            find_all(n, m, data, visited)
            # 그리고 끝났으면 빼고
            data.pop()
            # 방문 배열 리셋
            visited[i] = 0


n, m = map(int, input().split())
visited = [0] * (n + 1)
data = []
find_all(n, m, data, visited)