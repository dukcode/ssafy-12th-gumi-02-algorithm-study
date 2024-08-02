# 팰린드롬인지 확인하기

word = input()

# print(word[2])

for i in range(5):
    
    if word[i] == word[5 -1 - i]:
        print('1')
    else :
        print('0')