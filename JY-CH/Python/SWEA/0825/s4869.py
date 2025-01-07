# 종이 붙이기

def solve(num):
    if num < 20:
        return 1
    
    return solve(num-10) + solve(num-20)*2



T = int(input())
for tc in range(1, T+1):
    num = int(input())


    print(f'#{tc} {solve(num)}')
