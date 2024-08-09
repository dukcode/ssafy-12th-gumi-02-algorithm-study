# 9
# 7 4 2 0 0 6 0 7 0
# 낙차 구하기
# 상자의 높이를 가지고 있음
# 각 열의 꼭대기 상자들이 몇 칸 떨어지는지 계산하기
# 열의 오른쪽에 높이가 낮은 열이 몇개가 있는지 세면 됩니다.
# 그게 떨어지는 높이 >>> 그중에 제일 많이 떨어지는 높이 출력

N = int(input())
boxes = list(map(int, input().split()))
max_fall = 0 # 상자가 안떨어지면 0이라서 0으로 초기화

for i in range(N):
    # boxes[i] i열의 꼭대기 높이
    # i번째 상자가 몇 칸 떨어지는지 계산
    # i번째 상자보다 오른쪽에 있는 상자들 다 보기
    cnt = 0 # i번째 상자보다 낮게 있는 상자 개수 세는 변수
    for j in range(i+1, N):
        if boxes[i] > boxes[j]:
            cnt += 1

    # 상자가 떨어지는 높이 계산.
    # 최대값만 저장하면 됨.
    if cnt > max_fall:
        max_fall = cnt

print(max_fall)