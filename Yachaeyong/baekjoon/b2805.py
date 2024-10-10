# 나무 자르기
N, M = map(int, input().split())
trees = list(map(int, input().split()))

start = 1
end = max(trees)
ans = 0

while start <= end:
    mid = (start + end) // 2
    temp = 0
    for tree in trees:
        if tree > mid:
            temp += (tree - mid)
    # 가능한 mid의 최댓값을 찾아야하므로 M 만족해도 더 큰 값 찾기위해 또 탐색
    if temp >= M:
        ans = mid
        start = mid + 1
    else:
        end = mid - 1

print(ans)
