# 소수 찾기

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

