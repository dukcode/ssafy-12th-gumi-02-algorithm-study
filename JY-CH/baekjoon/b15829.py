# Hashing
import sys
input = sys.stdin.readline


# 1번 풀이
# dict = {
#     'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
#     'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
#     'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
#     'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
#     'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
#     'z': 26
# }


# n = int(input())
# data = list(input())

# result = 0
# m = 1234567891
# for i in range(n):
#     result += int(dict[data[i]] * ((31 ** i) % m)
# print(result)


n = int(input())
m = 1234567891
data = list(input())

# (A+B) mod M
result = 0
for i in range(n):
    result += (ord(data[i]) - 96) * (31** i)
result %= m

print(result)


# ((A mod M) + (B mod M)) mod M
result = 0
for i in range(n):
    result += (ord(data[i]) - 96) * ((31 ** i) % m)
    result %= m

print(result)


# 위에 풀이와 아래 풀이는 수학적 관점에서는 같다.
# 그러나 컴퓨터 시스템적으로 보았을때는 아래 코드가 최적화가 된 코드이다.
