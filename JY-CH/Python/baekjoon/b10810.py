# 공 넣기

# 문제가 어려워 보이긴 했는데
# 사실 리스트 짜고 값만 할당해주면 되는 문제라고 생각하고 접근은 했는데
# 진짜 문제는

n, m = map(int, input().split())

answer = [0] * (n + 1)
# print(answer)

for num in range(m):                          # 정확히 여기 3줄은 짰는데
    i, j, k = map(int, input().split())       # 도저히 배열을 어떻게 집어넣을지를 몰랐습니다.
    for num2 in range(i, j+1):                # 배열을 초기화 시킨다는건 생각도 못했어요.
        answer[num2] = k
        # print(answer)

# print(answer)

# 배열 초기화 하고 값을 할당을 못하니 아래식까지 뻗지도 못했습니다.
# 1 넣는 이유는 0번째 바구니는 없어서 그래요.
for i in range(1, len(answer)):
    print(answer[i], end=' ')


# 15분 초과, 찾아봄.
# 이 문제 ㄹㅇ 개지린다.
# 진짜 도저히 이해 안되면 주석 해놓은 print 다 돌려보면 이해가 빨라짐.
