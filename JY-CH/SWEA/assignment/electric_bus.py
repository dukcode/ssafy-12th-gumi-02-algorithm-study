# 전기 버스

# 함수 정의하고

def solve(lst, k, n, m):
    cnt = 0
    distance = k
    # 충전소 거리가 이동거리보다 멀면 0 반환
    for j in range(1, len(lst)):
        # if lst[j] - lst[j - 1] > k:
        #     return 0
        for i in range(1, n+1):
            distance -= 1
            # 충전소 도착했고 이동 가능거리가 남은거리와 같거나 많은경우 or 이동가능거리로 다음 충전소 도착가능한경우

            if i in lst:
                next_lst = next((lst for lst in lst if lst > i), n)
                if distance >= n - i or distance >= next_lst - i:
                    continue
            # 충전소 도착했는데 이동 가능거리가 남은거리보다 적은경우
            if i in lst and distance < n - i:
                distance = k
                cnt += 1
            # 종점 도착시
            if i == n:
                return cnt
                break
            # 충전소도 도착 못했는데 거리가 0 / 충전소가 0
            if (i not in lst and distance == 0) or m == 0:
                return 0
                break





t = int(input())
for tc in range(1, t+1):
    k, n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    result = solve(lst, k, n, m)
    print(f'#{tc} {result}')