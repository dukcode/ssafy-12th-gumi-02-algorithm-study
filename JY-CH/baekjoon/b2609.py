# 최대 공약수와 최소 공배수
import sys
input = sys.stdin.readline



n, m = map(int, input().split())

data = []
for i in range(1, n + 1):
    if n % i == 0:
        data.append(i)
    
data2 = []
for i in range(1, m + 1):
    if m % i == 0:
        data2.append(i)

divide_list = []
for i in range(len(data)):
    for j in range(len(data2)):
        if data[i] == data2[j]:
            divide_list.append(data[i])

divide = max(divide_list)
multiply = divide * (n // divide) * (m // divide)




print(divide)
print(multiply)




