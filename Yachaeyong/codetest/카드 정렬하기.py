import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
cards = []
for _ in range(N):
    num = int(input())
    heappush(cards, num)

print(cards)
total_sum = 0
while len(cards) > 1:
    a = heappop(cards)
    b = heappop(cards)

    tmp_sum = a + b
    total_sum += tmp_sum

    heappush(cards, tmp_sum)

print(total_sum)
