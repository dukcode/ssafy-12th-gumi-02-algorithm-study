for tc in range(1, 11):
    str_N, lst = map(str, input().split())
    N = int(str_N)
    num_lst = list(map(int, lst))

    while True:
        a = 0
        b = 0
        for i in range(len(num_lst) - 2 + 1):
            if num_lst[i] == num_lst[i + 1]:

                a = i
                b = i + 1
                j = 1
                while 0 <= i - j < len(num_lst) and 0 <= i + 1 + j < len(num_lst):
                    if num_lst[i - j] == num_lst[i + 1 + j]:
                        a = i - j
                        b = i + 1 + j
                        j += 1
                    else:
                        break

                del num_lst[a : b + 1]
                break
        else:
            break
    print(f'#{tc} {"".join(map(str,num_lst))}')
