# 문자열 비교

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()


# 문자열 비교를 할건데
# str2에 str1이 있는지 확인해야되니까
# str2안에서 str1을 이동 시켜서 체크하고
# 있으면 1, 없으면 0
# 길이가 같을 경우를 대비 1을 추가해서 범위 설정
    count = 0
    for i in range(len(str2) - len(str1) + 1):
        for j in range(len(str1)):
            if str1[j] != str2[i+j]:
                break
        else:
            count = 1

    print(f'#{tc} {count}')





