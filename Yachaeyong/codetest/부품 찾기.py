# 부품 찾기
def search(start, end, target):
    global ans

    if start > end:
        ans.append('no')
        return

    mid = (start + end) // 2

    if stock_list[mid] == target:
        ans.append('yes')
        return

    elif stock_list[mid] > target:
        return search(start, mid - 1, target)
    else:
        return search(mid + 1, end, target)

    ans.append('no')
    return


N = int(input())
stock_list = list(map(int, input().split()))
M = int(input())
hope_list = list(map(int, input().split()))

stock_list.sort()
ans = []
for item in hope_list:
    search(0, N - 1, item)

print(*ans)
