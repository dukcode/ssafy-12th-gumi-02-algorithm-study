# 수 정렬하기 3
import sys
input = sys.stdin.readline

n = int(input())
data = [0] * 10001
for _ in range(n):
    data[int(input())] += 1

for i in range(10001):
    if data[i]:
        for j in range(data[i]):
            print(i)

# 앞으로는 요구사항을 잘 읽고 이해한다음
# 문제에 명시해놓고 풀것.

# 배열을 n개씩 짤 경우
# 입력값이 n 이상 나오면 indexerror가 발생할 수 밖에 없다
# 문제에 답이 있었다..