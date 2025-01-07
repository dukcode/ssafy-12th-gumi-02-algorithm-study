# ACM 호텔

def find_room(h, w, n):
    # 층수 만큼 순회하면서 n에서 뺀다
    # 1호에서 시작
    room_number = 1
    # h 보다 n 이 작을때까지 while 드가자
    while True:

        # 남는 n과 h가 같으면
        # 빼면 0이다 의미가 없다
        if n == h:
            if room_number < 10:
                return str(n) + '0' + str(room_number)
            else:
                return str(n) + str(room_number)
        elif n < h:
            if room_number < 10:
                return str(n) + '0' + str(room_number)
            else:
                return str(n) + str(room_number)
        else:
            room_number += 1
            n -= h
            continue


t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    result = find_room(h,w,n)

    print(int(result))

# 1호 돌고 다음호로 진행
