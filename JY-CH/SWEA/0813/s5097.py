# 회전


T = int(input())
for tc in range (1, T + 1):
    # 시행 횟수 만큼 숫자갯수 받고 m번 이동 시킬거고
    N, M = map(int, input().split())
    # 리스트로 받아온 숫자들
    num_lst = list(map(int, input().split()))
    # 어차피 돌려봤자 갯수만큼 돌면 원래대로 돌아오니까?
    # 돌리는 횟수만큼 숫자 갯수를 나눈 나머지 만큼만 돌리자.
    C = M % N

    for i in range(C):
        data_one = num_lst.pop(0)
        num_lst.append(data_one)

    result = num_lst[0]

    print(f'#{tc} {result}')





