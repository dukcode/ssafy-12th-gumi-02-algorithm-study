T = int(input())
for tc in range(1, T+1):
    memory = list(input())
    n = ['0']*len(memory)
    cnt = 0
    for i in range(len(n)):
        if n[i] != memory[i]:
            n[i:] = memory[i]*len(n[i:])
            cnt += 1
    print(f'#{tc} {cnt}')