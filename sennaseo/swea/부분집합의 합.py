T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    def solve(arr):
        if len(arr) == N:
            if sum(arr) == K:
                return 1
            return 0

        last_num = 0
        ret = 0
        if len(arr) != 0:
            last_num = arr[-1] # 만약 last_num이 0이 아니라면 리스트의 마지막 숫자를 last_num으로 지정

        # subset_sum == K를 거르기 위한 과정
        for i in range(last_num+1, N+1):
            arr.append(i)
            ret += solve(arr)
            arr.pop()

        return ret

    print(f'#{tc} {solve([])}')