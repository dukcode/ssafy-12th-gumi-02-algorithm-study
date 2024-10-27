T = int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    count = 0
    for i in range(0,len(str2)-len(str1)+1):
        if str2[i:i+len(str1)] == str1:
            count += 1
        else:
            continue
    print(f'#{tc} {count}')