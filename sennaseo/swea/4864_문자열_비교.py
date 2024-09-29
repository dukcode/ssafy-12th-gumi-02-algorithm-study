T = int(input())


def comp_string(str1, str2):

    for i in range(M - N + 1):
        if str1 == str2[i : i + N]:
            return 1
    return 0


for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    N = len(str1)
    M = len(str2)

    result = comp_string(str1, str2)
    print(f"#{tc} {result}")
