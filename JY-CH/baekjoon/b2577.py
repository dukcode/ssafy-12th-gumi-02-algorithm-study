# 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

number = (a * b * c)

data = list(map(int, str(number)))
arr = [0] * 10

for i in range(len(str(number))):
    arr[data[i]] += 1

for i in range(len(arr)):
    print(arr[i])



