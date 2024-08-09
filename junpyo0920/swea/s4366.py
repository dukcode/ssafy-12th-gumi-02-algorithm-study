# 같은 10진수 하나를 표현하는 2진수와 3진수가 있는데 각각의 수의 자릿수 중 하나가 잘못되었을 때,
# 10진수가 무엇인지 찾아내는 문제

for tc in range(int(input())):
    bin_num = list(map(int, input()))
    tri_num = list(map(int, input()))
    
    bin_to_deci_list = []
    tri_to_deci_list = []

    for idx, num in enumerate(bin_num):
        new_bin = bin_num[:]
        new_bin[idx] = 0 if num else 1
        bin_to_deci_list.append(int(''.join(map(str, new_bin)), 2))

    for idx, num in enumerate(tri_num):
        new_tri = tri_num[:]
        for n in range(3):
            if n == num: continue
            new_tri[idx] = n
            tri_to_deci_list.append(int(''.join(map(str, new_tri)), 3))

    print(f'#{tc + 1} {(set(bin_to_deci_list) & set(tri_to_deci_list)).pop()}')