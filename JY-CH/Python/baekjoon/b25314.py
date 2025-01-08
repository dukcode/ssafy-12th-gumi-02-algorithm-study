# 코딩은 체육과목입니다.

num = int(input())

rep_word = 'long '

for i in range(num+1):
    if i % 4 == 0:
        repeat_number = i // 4
        pri_long = rep_word * repeat_number
# print(f'{pri_long.split()} int')
print(pri_long + 'int')



# 15분 초과

# 반복문 풀이

# num = int(input())

# answer = 'int'

# for i in range(num//4):
#     answer = 'long ' + answer
# print(answer)


# 그냥 풀이
# print(num//4*'long ' + 'int')



### long 뒤에 공백을 못만들어서 못풀었는데
### 그냥 long 뒤에 한칸 띄우고 지정하면 되는문제였다..;;