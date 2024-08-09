# 숫자 카드

# i와 index[i]의 값이 같다면 cnt에 +1?
# 일단 정의 ㄱ
def solve(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i] < lst[j]:
                lst[i], lst[j] = lst[j], lst[i]

    cnt = [0] * 10
    for i in range(10):
        for j in lst:
            if i == j:
                cnt[i] += 1

    max_cnt = 0
    max_idx = 0
    for i in range(10):
        if max_cnt <= cnt[i]:
            max_cnt = cnt[i]
            if max_idx < i:
                max_idx = i


    return f'{max_idx} {max_cnt}'





# 테스트케이스, 횟수랑 리스트 받아옴
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    num_lst = list(map(int, input()))
    result = solve(num_lst)
    print(f'#{tc} {result}')