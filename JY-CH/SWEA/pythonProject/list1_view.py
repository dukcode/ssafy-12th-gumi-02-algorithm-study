# 조망권을 가진 세대를 계산하는 빌딩의
# 양 옆 2칸 이내의 건물들 중에 가장 높은 빌딩의 높이 구하기
# 대상 건물의 위치 (2번 ~ N-3번)
# 대상 건물의 위치 : i, 주변 건물 : i-2,i-1,i+1,i+2
# i를 2 ~ N-3까지 반복
# i-2, i-1, i+1, i+2 : i번 건물에 조망권이 있는지 확인
#   조망권 더 해주기


# 건물 정보를 인자로 받아서, 조망권을 가진 세대수를 반환하는 함수
def solve(buildings):
    result = 0 # 조망권을 가진 세대수를 저장하는 변수
    # 건물을 2~N-3까지 반복
    for i in range(2, N-2): # i번 건물의 조망권 계산
        # i-2, i-1, i, i+1, i+2번 건물중에 가장높은 건물 찾기
        max_height = 0
        for j in range(i-2, i+3):
            if j == i:
                continue
            if max_height < buildings[j]:
                max_height = buildings[j]
        # 가장 높은 건물 찾았으니 조망권 세대수 계산하기
        # i번 건물이 주변 건물보다 높으면 조망권이 있음
        if buildings[i] > max_height:
            result += buildings[i] - max_height

    return result


for tc in range(1,11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = solve(buildings)
    print(f'#{tc} {result}')