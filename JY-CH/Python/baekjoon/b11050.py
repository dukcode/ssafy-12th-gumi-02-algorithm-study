# 이항 계수
import sys
input = sys.stdin.readline


def factorial(num):
    data = list(range(1, num + 1))
    result = 1
    for i in data:
        result *= i
    return result



n, k = map(int, input().split())

answer = int(factorial(n) / (factorial(k) * factorial(n - k)))
print(answer)