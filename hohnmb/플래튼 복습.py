T = 10

for tc in range(1, T+1):
    # 덤프를 진행할 횟수
    dump_count = int(input())
    # 건물들의 높이
    b_height = list(map(int,input().split()))
    # 덤프 진행 횟수만큼 반복함
    for _ in range(dump_count):
        # 최대 높이와 최소 높이 인덱스 초기화용
        max_height = 0
        min_height = 0
        # 건물들의 총 인덱스 길이는 100임. 길이 100에서 도는데
        for i in range(100):
            # 건물 높이의 초기 인덱스 0값이 건물 총 인덱스 1~100을 도는동안 초기인덱스 0값의 높이보다 크면
            if b_height[max_height] < b_height[i]:
                # 건물 초기 인덱스값을 큰값이랑 교환.
                # 교환하고 다음 값이 교환한값보다 클 경우에 또 교환.
                max_height = i
                # 위의 최대값과 똑같음. 건물인덱스 0의 높이보다 건물인덱스 i값이 작으면
                # 초기값 건물 인덱스0의 값을 더 작은 인덱스값의 높이랑 교환.
            if b_height[min_height] > b_height[i]:
                min_height = i
        # 건물들의 총 인덱스만큼 반복문을 돌고 나온 건물 인덱스값의 높이에서 가장 높은 건물은 값에 1을 빼고, 가장 작은 건물의 값에는 1을 더함.
        b_height[max_height] -= 1
        b_height[min_height] += 1
        # 평탄화를 진행한 건물들의 높이에서 최대값과 최소값을 다시 찾음.
        # 이 작업이 왜 필요하냐, 바로 위에서 해당 인덱스 최대값과 최소값에 해당하는 건물 높이 값을 건드려서 다시 최대값과 최소값을 찾을 필요가 있음.
        for k in range(100):
            if b_height[max_height] < b_height[k]:
                max_height = k
            if b_height[min_height] > b_height[k]:
                min_height = k
    # 출력.
    print(f'#{tc} {b_height[max_height] - b_height[min_height]}')