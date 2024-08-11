# https://www.acmicpc.net/problem/15649
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 찾는 문제

# arr에 1~N까지의 자연수를 중복없이 추가
def perm(arr, used):
    # M개를 찾으면 M개의 수가 들어있는 배열 출력
    if len(arr) == M:
        print(*arr)
        return

    for i in range(N):
        if not used[i]:  # i를 이전에 추가하지 않았으면,
            arr.append(i+1)  # arr에 i+1 추가 >>> i는 0부터 N-1까지 이므로
            used[i] = 1  # 사용 이력 추가
            perm(arr, used)  # M개 찾을 때 까지 추가
            arr.pop()  # 모든 경우의 수를 찾기 위해 최근에 추가된 요소 제거
            used[i] = 0  # 최근에 추가된 요소의 사용 이력 제거


N, M = map(int, input().split())
perm([], [0] * N)