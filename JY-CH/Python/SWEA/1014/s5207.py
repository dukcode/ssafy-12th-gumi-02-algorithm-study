def binary(target, key):

    direction = 0  # 1 : 왼쪽, 2: 오른쪽
    start = 0
    end = n - 1
    while start <= end:
 
  
        m = (start + end) // 2
     
        if target[m] == key:
           
            return True
       
        elif target[m] > key:  
            if direction == 1:
                break
            else:
                direction = 1 
                end = m - 1
        else: 
            if direction == 2:
                break
            else:
                direction = 2
                start = m + 1
    return False
 
t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    arr1.sort()
    result = 0
    for num in arr2:
        if binary(arr1, num):
            result += 1
    print(f'#{tc} {result}')