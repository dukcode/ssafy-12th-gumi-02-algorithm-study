# 두 전구

def check(a, b, c, d):
    start = max(a, c)
    end = min(b, d)
    ans = end - start
    if ans <= 0:
        ans = 0
    result_list.append(ans)


result_list = []
for tc in range(int(input())):
    x_start, x_end, y_start, y_end = map(int, input().split())
    check(x_start, x_end, y_start, y_end)

for idx, result in enumerate(result_list):
    print(f'#{idx+1} {result}')


# 이걸 이렇게도 출력할 수가 있구나