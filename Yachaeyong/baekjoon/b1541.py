# 잃어버린 괄호

exp = input().split('-')

temp = []

for e in exp:
    plus = 0
    data = e.split('+')
    for d in data:
        plus += int(d)
    temp.append(plus)
n = temp[0]
for i in range(1, len(temp)):
    n -= temp[i]

print(n)
