for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    
    ans = [[] * n for _ in range(n)]
    for _ in range(3):
        new_arr = [[0] * n for _ in range(n)]
        for x in range(n):
            new_line_i = []
            for y in range(n - 1, -1, -1):
                new_line_i.append(arr[y][x])
            new_arr[x] = new_line_i
            ans[x].append(''.join(map(str, new_line_i)))
        arr = new_arr
    
    print(f'#{tc + 1}')
    for i in range(n):
        print(' '.join(ans[i]))
