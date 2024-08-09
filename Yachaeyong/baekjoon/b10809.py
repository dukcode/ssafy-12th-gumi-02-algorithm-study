# 알파벳 찾기

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#1. for문으로 순회해서 인덱스 위치 반환하는 방식
#S = list(str(input()))
# for i in alphabet:
#     if i in S:
#         print(S.index(i), end=' ')
#     else:
#         print('-1', end=' ')

#2. 문자열.find()로 찾는 방식
S = input()

for x in alphabet:
    print(S.find(x), end=' ')