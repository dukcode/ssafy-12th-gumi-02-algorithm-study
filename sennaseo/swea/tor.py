# 범위 전체의 승자를 구하기 위해서
# 절반 범위의 승자 2명이 필요하다
# 1 가위 2바위 3보
# 0 1  2 3  4 5  6 7       8 9  10 11 12 13  14 15
# 1 1  2 3  3 2  1 3       1 2  3 1    1 3   3 2
#  0    3    4    6         9    11     12    14
#     0         6               9          12
#
#         0                         9
#
#                  9
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))


    def solve(i, j):
        # i == j 이면 사람이 한 명이다.
        if i == j:    #한 명이니까 내가 이긴거 (base case)
            return i

        winner1 = solve(i, (i + j) // 2)
        winner2 = solve((i + j) // 2 + 1, j)
        # winner1이 앞에 있어 이길 확률이 높으니까
        # winner1이 이겼다 치고
        # winner2가 이기는 경우만 결과 바꿔주기
        result = winner1
        # data[winner1]
        # data[winner2]
        # 승자 두 명 뽑았으니 가위바위보 결과 계산하기
        if data[winner1] == 1 and data[winner2] == 2:
            result = winner2
        elif data[winner1] == 2 and data[winner2] == 3:
            result = winner2
        elif data[winner1] == 3 and data[winner2] == 1:
            result = winner2

        return result

    print(f'#{tc} {solve(0, N - 1) + 1}')
    # 이 함수는 인덱스로 번호를 받았기 때문에
    # 실제 번호는 solve함수에 1을 더해주어야 함


