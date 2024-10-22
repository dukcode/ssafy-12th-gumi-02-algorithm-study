# 단어 정렬

import sys

N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
words = list(set(words))
words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
