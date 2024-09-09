def solve():
    max_i = 0
    min_i = N
    max_j = 0
    min_j = N
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "#":
                if i >= max_i:
                    max_i = i
                if i < min_i:
                    min_i = i
                if j >= max_j:
                    max_j = j
                if j < min_j:
                    min_j = j
    for i in range(min_i, max_i + 1):
        for j in range(min_j, max_j + 1):
            if arr[i][j] == ".":
                return "no"
    if max_i - min_i == max_j - min_j:
        return "yes"


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    result = solve()
    if result == "yes":
        print(f"#{tc} yes")
    else:
        print(f"#{tc} no")
