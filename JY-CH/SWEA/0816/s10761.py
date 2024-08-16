# 신뢰
T = int(input())
for tc in range(1, T+1):
    data = input().split()
    N = int(data.pop(0))
    # 이전 위치와 이전 버튼을 누른 시간 >>>
    B = 1   # 블루로봇 위치
    O = 1   # 오렌지 로봇 위치
    bt = 0
    ot = 0
    prev = data[0]
    for i in range(0, N*2, 2):
        robot = data[i] # 버튼을 누르는 로봇
        btn = int(data[i+1]) # 로봇이 눌러야 하는 버튼의 번호
        if robot == prev:
            # B : 이전 버튼을 누른 위치
            # bt : 이전 버튼을 누른 시간
            # btn : 이번에 눌러야 하는 버튼 번호
            bt += abs(B-btn) + 1
            B = btn
        else:
            ot += abs(O - btn) + 1
            O = btn
    else:   # 이전 버튼을 누른 로봇과 다른 로봇이 버튼을 누름
        if robot == 'B':
            # 미리가서 기다리는 경우,
            # 이번 버튼을 누르는 시간
            if bt + abs(B-btn) + 1 <= ot:
                bt = ot + 1
            else:   # 이동 마저 다하고 누르는 경우
                bt = bt + abs(B-btn) + 1
            B = btn
            # 다른 로봇이 버튼을 누르고 나서도, 아직 이동중인 경우
        else:

    prev = robot
