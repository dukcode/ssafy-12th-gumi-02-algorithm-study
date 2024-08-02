t = int(input())




for tc in range(1, t + 1):
    cnt = int(input())
    lst = list(map(int, input().split()))
    num_lst = [0] * 10
    for i in range(cnt):
        low_idx = i
        for j in range(i+1, cnt):
            if lst[low_idx] > lst[j]:
                low_idx = j
        lst[i], lst[low_idx] = lst[low_idx], lst[i]



    a = 0
    b = 0
    for i in range(5):
        num_lst[a] = lst[-b-1]
        num_lst[a+1] = lst[b]
        a += 2
        b += 1
    
    print(f'#{tc} ', end='')
    print(*num_lst)