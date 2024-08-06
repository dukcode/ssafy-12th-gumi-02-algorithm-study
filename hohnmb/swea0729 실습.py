T = int(10)
 
for tc in range(1, T+1):
    n = int(input())
    h = list(map(int,input().split()))
    # 높이가 0 0 254 185 76 227 84 175 0 0 일때,
    count = 0
    # 맨 앞 두칸과 맨 뒤 두칸은 0이니까 제외함.
    for i in range(2, n-2):
        # 양 옆으로 2칸 이상 확보가 되야 조망권이 확보됨.
        round_top = max(h[i-2],h[i-1],h[i+1],h[i+2])
        # 근처의 가장 높은 건물의 높이보다 클 경우
        # 그 건물의 높이만큼 뺌. 그리고 카운트에 저장.
        if h[i] > round_top :
            count += h[i] - round_top
    print(f'#{tc} {count}')