# 팰린드롬인지 확인하기

word = input()
n = len(word)

# print(word[2])

# for i in range(5):
    
#     if word[i] == word[5 -1 - i]:
#         print('1')
#     else :
#         print('0')

for i in range(n//2):
    if word[i] != word[n-1-i]:
        print(0)
        break
else:
    print(1)