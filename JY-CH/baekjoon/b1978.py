# 소수 찾기

<<<<<<< HEAD
def check(data):
    cnt = 0

    for i in range(len(data)):
        if data[i] == 1 or data[i] == 2 or data[i] == 3:
            pass
        for j in range(2, data[i]):
        
            if data[i] % j == 0:
                continue
            else:
                cnt += 1
                break
    return cnt


n = int(input())
num = list(map(int, input().split()))
result = check(num)
print(result)

=======

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
>>>>>>> 20666800d475f9914317fe48246e7ec3c0f04d8e
