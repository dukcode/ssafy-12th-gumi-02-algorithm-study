# # 이진수2
def solve(num):

    global check
    global cnt
    global sth

    if abs(cnt) > 12:
        print('overflow')
        return

    if num < (1*2**cnt) or num == 0:
        cnt -= 1
        if num == 0:
            for i in range(1, abs(cnt)):
                sth += str(check[i])
            print(sth)
            return 
        else:
            solve(num)
    else:
        check[abs(cnt)] += 1
        solve(num-(1*2**cnt))






T = int(input())
for tc in range(1, T+1):
    num = float(input())
    cnt = 0
    check = [0] * 13
    sth = ''


    print(f'#{tc} ', end='')
    solve(num)

