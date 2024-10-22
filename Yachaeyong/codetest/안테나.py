import sys

input = sys.stdin.readline

N = int(input())
houses = list(map(int, input().split()))
houses.sort()

ans = houses[(N - 1) // 2]

print(ans)
