# 국영수
import sys
input = sys.stdin.readline

n = int(input())

arr = []

for _ in range(n):
    name, korean, english, math = input().split()
    arr.append((name, int(korean), int(english), int(math)))




arr.sort(key = lambda element:element[0])
arr.sort(key = lambda element:element[3], reverse=True)
arr.sort(key = lambda element:element[2])
arr.sort(key = lambda element:element[1], reverse=True)

for idx in range(n):
    print(arr[idx][0])


