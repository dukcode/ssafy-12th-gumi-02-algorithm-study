# 점수들이 주어지고 가장 빈도수가 높은 점수를 출력하는 문제
# 단, 최빈수가 여러 개 일 경우, 가장 높은 점수를 출력

for _ in range(int(input())):
    tc = int(input())
    arr = list(map(int, input().split()))
    # 각 점수를 count할 수 있는 배열 생성, 점수는 0점 이상 100점 이하이므로 배열의 크기는 101
    counts = [0] * 101
    # 점수들을 순회하며 개수 세기
    for score in arr:
        counts[score] += 1
    
    max_idx = 0
    # 점수의 개수가 담긴 배열을 순회하며 개수가 가장 큰 점수(counts의 index와 같음) 탐색
    for i in range(101):
        max_idx = i if counts[max_idx] <= counts[i] else max_idx
    
    print(f'#{tc + 1} {max_idx}')
