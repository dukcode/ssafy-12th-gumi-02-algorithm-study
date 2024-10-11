# 수 찾기

def binary(data, target):
    start = 0
    end = len(data)

    while start < end:
        half = (start + end) // 2
        if data[half] == target:
            return 1
        
        if data[half] > target:
            end = half
        else:
            start = half + 1

    return 0


n = int(input())
data = sorted(list(map(int, input().split())))
m = int(input())
check = list(map(int, input().split()))



for idx in range(m):
    print(binary(data, check[idx]))


