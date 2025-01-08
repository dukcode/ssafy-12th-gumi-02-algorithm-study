from collections import deque

import sys
input = sys.stdin.readline

# 카드 2

n = int(input())

deck = deque(list(range(1, n + 1)))



while True:
    if len(deck) == 1:
        answer = deck.pop()
        break
    
    deck.popleft()
    if len(deck) == 1:
        answer = deck.pop()
        break
    num = deck.popleft()
    deck.append(num)

print(answer)

    
