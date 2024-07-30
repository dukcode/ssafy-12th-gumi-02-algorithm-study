#단어의 개수

#print(len(input().split())) 하면 쉬운데
#함수 최대한 안 쓰려고 해봄
#처음엔 ' '기준으로 단어 개수 셌는데
#맨 앞과 맨 뒤 공백도 단어로 처리해서 틀림

string = input().split()
count = 0

for i in string:
    count += 1

print(count)