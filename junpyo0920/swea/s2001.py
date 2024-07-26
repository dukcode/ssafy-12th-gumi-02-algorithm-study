for tc in range(int(input())):
    len_field, len_fly_killer = map(int, input().split())
    field = [list(map(int, input().split())) for _ in range(len_field)]
    fly_killer = [(x, y) for x in range(len_fly_killer) for y in range(len_fly_killer)] # tuple comprehension은 tuple((x, y) ...)으로 작성해야 함

    ans = 0
    for y in range(len_field):
        for x in range(len_field):
            temp_ans = 0

            for pos in fly_killer:
                pos_y = y + pos[0]
                pos_x = x + pos[1]
                if pos_y < len_field and pos_x < len_field:
                    temp_ans += field[pos_y][pos_x]
            
            ans = max(ans, temp_ans)
    
    print(f'#{tc + 1} {ans}')