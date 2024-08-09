for tc in range(int(input())):
    mem = list(input())
    init_mem = ['0'] * len(mem)

    cnt = 0
    for i in range(len(mem)):
        if mem[i] != init_mem[i]:
            for j in range(i, len(init_mem)):
                init_mem[j] = mem[i]
            cnt += 1
    print(f'#{tc + 1} {cnt}')