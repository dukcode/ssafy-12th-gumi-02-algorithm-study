for tc in range(int(input())):
    data = input().split()
    button_cnt = int(data[0])
    orders = []
    time = 0
    o_buttons = [0] * 101
    b_buttons = [0] * 101
    o = 0
    b = 0

    for i in range(button_cnt):
        color, button_pos = data[(i*2)+1], int(data[(i*2)+2])
        orders.append((color, button_pos))
        if color == "O":
            o_buttons[button_pos] = 1
        else:
            b_buttons[button_pos] = 1

    moves = 0
    while orders:
        if not o_buttons[o] and not b_buttons[b]:
            moves += 1
            o += 1
            b += 1
        elif o_buttons[o]:
            if orders[0][0] == "O":
                moves += 1
                orders.pop(0)
            else:
                if b_buttons[b]:
                    moves += 1
                    orders.pop(0)
                else:
                    moves += 1
                    b += 1
        elif b_buttons[b]:
            if orders[0][0] == "B":
                moves += 1
                orders.pop(0)
            else:
                if o_buttons[o]:
                    moves += 1
                    orders.pop(0)
                else:
                    moves += 1
                    o += 1
    print(moves)

# 버튼을 눌러야 할 때까지 이동
# 버튼을 눌러야 할 순서 확인
#
