# 알파벳 찾기

word = str(input())
alphabet = 'abcdefghijklmnopqrstuvwxyz'
# print(len(alphabet))
# print(alphabet[2])

for i in range(len(alphabet)):
    if alphabet[i] in word:
        print(word.index(alphabet[i]))
    else:
        print('-1')


# print(word.index('a'))