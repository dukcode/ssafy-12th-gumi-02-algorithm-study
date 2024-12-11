# 소수 찾기
def find(number):
    if number > 2:
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    elif number == 2:
        return True
    else:
        return False
            





n = int(input())
data = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if find(data[i]):
        cnt += 1
print(cnt)

