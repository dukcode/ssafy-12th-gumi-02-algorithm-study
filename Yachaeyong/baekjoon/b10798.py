# 세로 읽기

arr = [list(map(str, input().strip())) for _ in range(5)]

col_list = []

for j in range(15):
    for i in range(5):
        # 열 번호가 행 길이와 같으면 빈 칸이라는 의미
        if j < len(arr[i]):
            col_list.append(arr[i][j])

result = ''.join(col_list)
print(result)