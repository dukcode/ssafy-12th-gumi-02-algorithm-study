T = int(input())
for tc in range(1, T + 1):
    memory = list(map(int, str(input())))

    reset = [0] * len(memory)

    cnt = 0
    for i in range(len(memory)):
        if reset[i] != memory[i]:
            cnt += 1
            for j in range(i, len(memory)):
                reset[j] = memory[i]

    print(f"#{tc} {cnt}")
