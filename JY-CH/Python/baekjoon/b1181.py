# 단어 정렬

# 길이가 짧은것부터
# 길이가 같으면 사전순으로
import sys
input = sys.stdin.readline

# 중복단어 제거




n = int(input())
data = set()
for _ in range(n):
    data.add(input().strip())

data = list(data)


# dict = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
#     'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#     'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
#     'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
#     'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#     'z': 26
# }

# 일단 길이대로 정렬
sorted_data = sorted(data, key=lambda x: (len(x), x))



for word in sorted_data:
    print(word)
# print(a)


