# 증가하는 사탕 수열

# 상자 a,b,c 3개
# 순증가하기를 원함 a < b < c
# a b c 최소 1
# 무조건 까는거 말고는 못함.
# 만족이 가능한지 판단, 된다면 몇개나 먹어야하는지.

# 안되는 걸 찾아야함.

# b c 는 1 이면 아웃.


def check(lst):
    cnt = 0
    idx = 0
    if lst[idx+1] < 2 or lst[idx+2] < 3:
        return -1

    if lst[idx+1] >= lst[idx+2]:
       cnt += lst[idx+1] - (lst[idx+2] - 1)
       lst[idx+1] = lst[idx+2] - 1

    if lst[idx] >= lst[idx+1]:
       cnt += lst[idx] - (lst[idx+1] - 1)
       lst[idx] = lst[idx+1] - 1

    return cnt





for tc in range(int(input())):
    candy = list(map(int, input().split()))
    result = check(candy)
    print(f'#{tc+1} {result}')