t = int(input())
for tc in range(1, t+1):
    n = int(input())
    n_list = list(map(int, input().split()))

    for i in range(n-1, 0, -1):
        for j in range(0, i):
            if n_list[j] < n_list[j+1]:
                n_list[j], n_list[j+1] = n_list[j+1], n_list[j]
    print(n_list)


    answer = [0] * 10
    a = 0
    b = 0
    for _ in range(5):
        answer[a] = n_list[b]
        answer[a+1] = n_list[-b-1]
        a += 2
        b += 1

    print(f'#{tc}', *answer)
