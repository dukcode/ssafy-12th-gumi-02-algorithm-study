T = 10
for tc in range(1, T+1):
    N, arr = input().split()
    N = int(N)
    code = []
    for i in range(N):
        code.append(arr[i])
    i = 0
    while i < len(code)-1:
        if code[i] == code[i+1]:
            code.pop(i)
            code.pop(i)
            i -= 1
        else:
            i+=1
    result = ''
    for i in code:
        result += i
    print(f'#{tc} {result}')