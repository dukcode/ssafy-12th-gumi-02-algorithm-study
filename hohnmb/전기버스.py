def solve():
    position = 0

    count = 0

    while True:
        position += k
        if position >= n:
            return count
        is_find = False
        for i in range(position,position-k,-1):
            if stops[i] == 1:
                is_find = True
                count += 1
                position = i
                break
        
        if not is_find:
         return 0











T = int(input())

for tc in range(1, T+1):
    k,n,m = map(int,input().split())
    bus_station = list(map(int,input().split()))

    stops = [0] * (n)
    for num in bus_station:
        # 스탑스의 i인덱스(충전소 위치) 가 1로 설정됨.
        stops[num] = 1
    result = solve()

    print(f'#{tc} {result}')
    