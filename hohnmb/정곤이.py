T = int(input())
for tc in range(1, T + 1):
    N = int(input())  # 4
    arr = list(map(int, input().split()))
    max_v = -1
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            x = arr[i] * arr[j]
            for k in range(len(str(x)) - 1):
                # k = 0, 1
                if str(x)[k+1] < str(x)[k]:
                    break
            else:
                max_v = max(max_v, x)
 
    print(f'#{tc} {max_v}')