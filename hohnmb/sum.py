for i in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    sum = [0]*202 
    for i in range(100):
        for j in range(100):
                sum[i] += arr[i][j]
                sum[i+100] += arr[j][i]
                if i == j:
                    sum[200]+= arr[i][j]
                if i == 99-j:
                    sum[201]+= arr[i][j]
    max = 0
    for index in range(len(sum)):
        if max < sum[index]:
            max = sum[index]
 
    print(f'#{tc} {max}')