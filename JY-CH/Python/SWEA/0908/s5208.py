# 전기 버스2

def solve(bus_stop, battery):
    # 충전횟수 변수
    cnt = 0
    # 현재위치, 이동가능거리 변수
    # 이동가능거리의 경우 첫 위치 충전기만큼 받고감
    potential = battery[0]
    pos = 0

    while True:

        # 다음 위치, 다음 이동가능거리 변수 설정
        next_pos = 0
        next_potential = 0

        # 후보지 및 후보지 이동가능거리 탐색
        for candidate_pos in range(pos + 1, potential + 1):
            candidate_potential = candidate_pos + battery[candidate_pos]
            # 후보지 이동가능거리가 크거나 같을경우
            # 종료하고 충전횟수 + 1
            # -1 안하면 인덱스 스타트가 0이라 딱뎀 처리가 안됨.
            if candidate_potential >= len(bus_stop) -1:
                return cnt + 1
            # 후보지 이동가능거리가 다음이동가능거리가보다 크면
            # 전부 교체하고
            if candidate_potential > next_potential:
                next_pos = candidate_pos
                next_potential = candidate_potential
        #충전횟수 1 추가한다음
        #이동가능거리, 위치 변경
        cnt += 1
        potential = next_potential
        pos = next_pos





for tc in range(int(input())):
    battery = list(map(int, input().split()))
    bus_stop = list(range(battery.pop(0)))
    battery.append(0)
    result = solve(bus_stop, battery)
    print(f'#{tc+1} {result}')