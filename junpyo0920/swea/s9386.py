# 0과 1로 이루어진 수열에서 연속된 1의 개수 중 최댓값을 찾는 문제
for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input()))
    ans = 0

    # 수열을 수열의 길이만큼 순회하며 연속된 1의 개수 찾기
    cnt = 0
    for i in range(n):
        # i번째 요소가 1이면 카운트 1 증가
        if arr[i]:
            cnt += 1
            # 마지막 요소일 때만 최댓값과 카운트 비교
            if i == n - 1:
                ans = cnt if ans < cnt else ans
        # i번째 요소가 0이면 최댓값과 카운트 비교, 카운트 초기화
        else:
            ans = cnt if ans < cnt else ans
            cnt = 0

    print(f'#{tc + 1} {ans}')
