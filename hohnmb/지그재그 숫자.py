T = int(input())

for tc in range(1,T+1):
    n = int(input())
    sum_value = 0
    for i in range(1,n+1):
        if i%2 == 1 :
            sum_value += i
        else:
            sum_value -= i
    print(f'#{tc} {sum_value}') 
