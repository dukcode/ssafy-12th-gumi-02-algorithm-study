# N x N 크기의 행렬이 주어질 때,
# 마름모 내부의 값을 모두 더하는 문제
# 마름모 별 찍기와 유사

for tc in range(int(input())):
    len_matrix = int(input())
    matrix = [list(map(int, input())) for _ in range(len_matrix)]
    start, end = len_matrix // 2, len_matrix // 2

    ans = 0
    for y in range(len_matrix) :
        for x in range(start, end + 1) :
            ans += matrix[y][x]

        if y < len_matrix // 2 :
            start -= 1
            end += 1
        else :
            start += 1
            end -= 1

    print(f'#{tc + 1} {ans}')