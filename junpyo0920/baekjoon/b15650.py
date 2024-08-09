# https://www.acmicpc.net/problem/15650
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 조합을 찾는 문제

# 1이 M개 있는 bit 찾기
def comb(bit, idx=0, cnt=0):
    # 1이 M개면 끝
    if cnt == M:
        # arr과 bit를 비교하며 사용된 요소 출력
        for i in range(N):
            if bit[i]:
                print(arr[i], end=" ")
        print()
        return

    # N-1까지 추가했는데 1의 개수가 1이 아닐 경우
    if idx == N:
        return

    # 오름차순으로 출력해야 하므로 역순으로 탐색
    for i in range(1, -1, -1):
        bit[idx] = i  # i에 따라 사용하거나 사용하지 않거나
        comb(bit, idx+1, cnt+i)  # 다음 idx로 이동, 현 idx의 요소를 사용하면 cnt+1 아니면 cnt+0
        bit[idx] = 0  # 모든 경우의 수를 찾기 위해


N, M = map(int, input().split())
arr = [i for i in range(1, N+1)]
comb([0] * N)
