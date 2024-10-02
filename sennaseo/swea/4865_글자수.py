T = int(input())

for tc in range(1, T + 1):

    str1 = input()
    str2 = input()

    lst_str1 = []
    for i in str1:
        lst_str1 += i

    lst_str2 = []
    for j in str2:
        lst_str2 += j

    max_val = 0
    for x in range(len(lst_str1)):
        count_lst = 0
        for j in range(len(lst_str2)):
            if lst_str1[x] == lst_str2[j]:
                count_lst += 1

        if count_lst > max_val:
            max_val = count_lst

    print(f"#{tc} {max_val}")
