T = int(input())
for tc in range(1, T + 1):
    arr = input().split()
    cur_time = 0
 
    # blue 버튼 위치, orange 버튼 위치, 로봇의 실행 순서
    blue_btn, orange_btn, order = [], [], []
 
    for i in range(1, len(arr), 2):
        robot, btn_pos = arr[i], int(arr[i+1])
        order.append(robot)
        if robot == 'B': blue_btn.append(btn_pos)
        else: orange_btn.append(btn_pos)
 
    orange_pos = blue_pos = 1
    while order:  # 수열이 빈리스트가 아닐 동안
        cur_time += 1
        type = order[0]
 
        if blue_btn: # blue 로봇이 눌러야할 버튼이 있으면
            if blue_pos < blue_btn[0]:
                blue_pos += 1
            elif blue_pos > blue_btn[0]:
                blue_pos -= 1
            else:
                if type == 'B':
                    order.pop(0)
                    blue_btn.pop(0)
        if orange_btn:      # orange 로봇이 눌러야할 버튼이 있으면
            if orange_pos < orange_btn[0]:
                orange_pos += 1
            elif orange_pos > orange_btn[0]:
                orange_pos -= 1
            else:
                if type == 'O':
                    order.pop(0)
                    orange_btn.pop(0)
 
    print(f'#{tc} {cur_time}')