def strfry(str1, str2):
    new_str2 = list(str2)
    try:
        for char in str1:
            new_str2.pop(new_str2.index(char))
        if not new_str2:
            return True
        else:
            return False
    except:
        return False


def strfry2(str1, str2):
    arr_str1, arr_str2 = sorted(list(str1)), sorted(list(str2))
    return arr_str1 == arr_str2


for tc in range(int(input())):
    str1, str2 = input().split()
    print("Possible" if strfry(str1, str2) else "Impossible")