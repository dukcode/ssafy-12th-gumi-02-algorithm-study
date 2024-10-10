T  = int(input())
 
for tc in range(1, T+1):
    stick = list(input())
    n = 0
    result = 0
 
    for i in range(len(stick)):
        if stick[i] == '(':
            if stick[i+1] == '(':
                n += 1
                result += 1
            else:
                result += n
        else:
            if stick[i-1] == ')':
                n -= 1
    print(f'#{tc} {result}')