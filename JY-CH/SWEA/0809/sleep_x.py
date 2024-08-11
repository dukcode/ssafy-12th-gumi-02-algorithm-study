# 새로운 불면증 치료법


# tc 받고 n도 받고
t = int(input())
for tc in range(1, t+1):
    n = int(input())

# while문 돌리고
    
    k = 0
    lst = []
    while True:
        if len(set(lst)) == 10:
            print(f'#{tc} {k*n}')
            break
        else:
            k += 1

        num_lst = list(map(int, str(k*n)))
        for i in num_lst:
            lst.append(i)

        
        

