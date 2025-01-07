# 길 찾기

def dfs():
    A, B = 0, 99
    stack = [A]
    visited = [0] * 100
    visited[A] = 1

    while stack:
        now = stack[-1]
        if now == B:
            return 1

        for i in nums[now]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
                break
        else:
            stack.pop()

    return 0






for _ in range(1, 11):
    tc, E = map(int, input().split())
    nums = [[] for _ in range(100)]
    lst = list(map(int, input().split()))
    for i in range(E):
        nums[lst[2*i]].append(lst[2*i+1])


    print(f'#{tc} {dfs()}')
