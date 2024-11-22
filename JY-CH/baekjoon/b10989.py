# 수 정렬하기 3
import sys
input = sys.stdin.readline

data = []
n = int(input())
for i in range(n):
    data.append(int(input()))
    if len(data) >= 2:
        while True:
            for j in range(1, i + 1):
                if data[j - 1] > data[j]:
                    data[j - 1], data[j] = data[j], data[j - 1]

print(data)