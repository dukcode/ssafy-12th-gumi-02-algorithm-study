# 나머지
num =[]
#입력 값 42로 나눈 나머지 바로 빈 리스트 num에다가 넣으면 중복X
for i in range(10):
    n = int(input()) % 42
    if n not in num:
        num.append(n)

print(len(num))


#원래는 for문으로 입력값 리스트 만들고, 42로 나눈 값 저장하고
#하나하나 대조해서 다르면 카운트 +1 할려했음.
# count = 0 

# for _ in range(10):
#     num.append(int(input()))

# for i in range(len(num)):
#     num[i]= num[i] % 42

# for j in range(len(num)):
#     if num[j] != num[j+1]:
#         count += 1

# print(count)
