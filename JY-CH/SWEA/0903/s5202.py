# 화물 도크

t = int(input())
for tc in range(1, t+1):
    work_cnt = int(input())
    lst = []
    for _ in range(work_cnt):
        start, end = map(int, input().split())
        lst.append([start, end])
        lst.sort(key=lambda x: x[1])

    cnt = 0
    last_end = 0
    for start, end in lst:
        if last_end <= start:
            cnt += 1
            last_end = end

    print(f'#{tc} {cnt}')


