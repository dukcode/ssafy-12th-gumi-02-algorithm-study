# 글자수

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    max_cnt = 0
    for i in range(len(str1)):
        cnt = 0
        for j in range(len(str2)):
            if str2[j] == str1[i]:
                cnt += 1

        if cnt > max_cnt:
            max_cnt = cnt

    print(f'#{tc} {max_cnt}')
