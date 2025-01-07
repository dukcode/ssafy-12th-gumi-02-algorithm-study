import sys
sys.stdin = open('sample_input.txt', 'r')



# 함수를 정의해보자

def solve(buildings):
    result = 0  # 결과 값을 남겨줄 소중한놈

    # 건물 높이 돌리기
    # 일단 중간애가 제일 높아야됨
    for i in range(2, N-2): # 2~8
        max_height = 0
    # 그래서 왼쪽2개, 오른쪽2개 비교 해서 최대높이에 할당하고
        for build in (buildings[i-2], buildings[i-1], buildings[i+1], buildings[i+2]):
            if max_height < build:
                max_height = build
    # 중간놈 높이랑 비교했을때 중간놈이 높으면
    # 높은만큼 결과값에 더해주고 반환
        if buildings[i] > max_height:
            result += buildings[i] - max_height

    return result

for tc in range(1,11):
    N = int(input())
    buildings = list(map(int, input().split()))
    result = solve(buildings)
    print(f'#{tc} {result}')
