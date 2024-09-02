'''
5 8 3
2 4 5 4 6
'''

# 내 답안

n, m, k = map(int, input().split())
data = sorted(list(map(int, input().split())))

m_cnt = 0
k_cnt = 0
ans = 0

while m_cnt != m:
    if k_cnt != k:
        ans += data[-1]
        k_cnt += 1
    else:
        ans += data[-2]
        k_cnt = 0
    m_cnt += 1

print(ans)

# 모범 답안

first = data[n-1]
second = data[n-2]

cnt = m // (k+1) * k  # 가장 큰 수를 더할 횟수
cnt += m % (k+1)  # m이 k+1로 나누어 떨어지지 않을 경우, 나머지 만큼 더 더해짐
cnt2 = m - cnt  # 두 번째로 큰 수르 더할 횟수 == m // k+1

answer = first * cnt + second * cnt2
print(answer)