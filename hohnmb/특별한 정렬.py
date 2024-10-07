T = int(input())
for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    lst.sort()
    sorted_lst = []
    for _ in range(5):
        sorted_lst.append(lst.pop(-1))
        sorted_lst.append(lst.pop(0))
    print(f'#{tc} ', end='')
    print(*sorted_lst)