n = int(input())

exp_dates = list(map(int, input().split()))
usage_plans = list(map(int, input().split()))

arr = [[] for _ in range(n)]

for i in range(n):
    arr[i] = [usage_plans[i], exp_dates[i]]

arr.sort()

ans = 0
last_max_exp = 0
temp_max_exp = 0
for i in range(n):
    # 만료일이 사용일 보다 커야 함
    if arr[i][0] > arr[i][1]:
        diff = arr[i][0] - arr[i][1]
        delay_count = diff // 30 + (1 if diff % 30 else 0)

        arr[i][1] += 30 * delay_count
        ans += delay_count

    # 이전 사용 예정일 기프티콘들의 최대 만료일 보다 현재 사용 예정일 기프티콘의 만료일이 커야 함
    if i > 0 and arr[i][1] < last_max_exp:
        new_diff = last_max_exp - arr[i][1]
        additional_delay_count = new_diff // 30 + (1 if new_diff % 30 else 0)

        arr[i][1] += 30 * additional_delay_count
        ans += additional_delay_count

    temp_max_exp = max(temp_max_exp, arr[i][1])

    if i + 1 < n and arr[i][0] != arr[i + 1][0]:
        last_max_exp = temp_max_exp

print(ans)
