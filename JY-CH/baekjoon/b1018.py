# 체스판 다시 칠하기

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# m * n
data = [input() for _ in range(n)]

# wb 시작패턴, bw 시작패턴
wb = [ 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW' ] 
bw = [ 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB', 'BWBWBWBW', 'WBWBWBWB' ]

# 돌리면서 확인
min_count = 99999999
for i in range(n - 7):
    for j in range(m - 7):
        b_start_count = 0
        w_start_count = 0
        for a in range(8):
            for b in range(8):
                if data[i + a][j + b] != wb[a][b]:
                    b_start_count += 1
                if data[i + a][j + b] != bw[a][b]:
                    w_start_count += 1
        min_count = min(min_count, b_start_count, w_start_count)

print(min_count)
    
    
