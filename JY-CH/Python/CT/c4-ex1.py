# 상하좌우

# L = (0, -1)
# R = (0, 1)
# U = (-1, 0)
# D = (1, 0)

N = int(input())
move = input().split()

arr = [[0] * N for _ in range(N)]
y, x = 0, 0
current = arr[y][x]

for i in range(len(move)):
    if move[i] == 'R':
        x += 1
    elif move[i] == 'L':
        x -= 1
    elif move[i] == 'U':
        y -= 1
    elif move[i] == 'D':
        y += 1

    if x < 0:
        x = 0
    if y < 0:
        y = 0

# 문제에선 1부터 시작하는데 인덱스는 0부터 시작하니까
# 값에서 1 더해줘야함.
print(y+1, x+1)


# 예외 생각 안해봄.





