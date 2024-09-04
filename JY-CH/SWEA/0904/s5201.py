# 컨테이너 운반

for tc in range(int(input())):
    n, m = map(int, input().split())
    weight = sorted(list(map(int, input().split())), reverse=True)
    truck = sorted(list(map(int, input().split())), reverse=True)

    print(weight, truck)
    cnt = 0
    for t in truck:
        while weight:
            w = weight.pop(0)
            if t >= w:
                cnt += w
                break

    print(f'#{tc+1} {cnt}')