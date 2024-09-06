T = int(input())
for _ in range(T):
    tc = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    num = set(arr)
 
    max_v = 0
    for i in num:
        if arr.count(i) >= arr.count(max_v):
            max_v = i
 
    print(f'#{tc} {max_v}')