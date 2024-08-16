# 파리 퇴치

# N * N 행렬에서 M * M 영역을 돌면서 합을 구하고
# 그 합중에서 최대 값을 출력

T = int(input())
for tc in range(1,T+1):
    N, M = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(N)]
    # 행에서 시작점 찾기
    max_sum = 0
    for i in range(N-M+1):
        for j in range(N-M+1):  # (i, j) >>> 파리채 영역 시작점
            # 시작점에서 M*M 크기의 영역 순회
            tmp_sum = 0
            for a in range(i, i+M):
                for b in range(j,j+M):
                    tmp_sum += data[a][b]
            if tmp_sum > max_sum:
                max_sum = tmp_sum
    print(f'#{tc} {max_sum}')

