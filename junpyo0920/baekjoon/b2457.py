n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

cnt = 0
i = 0
cur_end = (3, 1)

while i < n:
    s_month, s_date, e_month, e_date = data[i]
    if (s_month, s_date) <= cur_end < (e_month, e_date):
        max_end = (e_month, e_date)
        while i < n-1:
            ns_month, ns_date, ne_month, ne_date = data[i + 1]
            if cur_end < (ns_month, ns_date):
                break
            if max_end < (ne_month, ne_date):
                max_end = (ne_month, ne_date)
            i += 1

        cnt += 1
        cur_end = max_end

        if cur_end > (11, 30):
            print(cnt)
            exit()
    i += 1

print(0)
