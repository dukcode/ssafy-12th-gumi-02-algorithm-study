# 파스칼 삼각형
# 파스칼 삼각형의 row행을 그리는 역할
def solve(row, arr):
    # 재귀가 더이상 호출 되지 않는 시점
    if row == n:
        return
    # row + 1 개의 열에 숫자 채우기
    for j in range(row + 1):
        # 첫 열은 항상 1, 아니라면 이전행에서 값을 구해야 함.
        if j == 0:
            arr[row][j] = 1
        else:
            # 이전행 arr[row-1]
            # j번 열을 채우기 위해서는 이전행 j, j-1열의 값이 필요
            arr[row][j] = arr[row-1][j] + arr[row-1][j-1]
    solve(row+1, arr)






t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]
    solve(0,arr)
    print(f'#{tc}')
    for i in range(n):
        for j in range(i+1):
            print(arr[i][j], end=' ')
        print()