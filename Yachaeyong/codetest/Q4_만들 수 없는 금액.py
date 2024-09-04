# 만들 수 없는 금액

# 일단 오름차순 정렬.
# 만들 금액을 타겟을 설정하고 내가 가지고 있는 동전으로
# 타겟을 만들 수 있는지 확인 하고 업데이트.
# 타겟보다 가진 동전이 더 크면 못 만듦

N = int(input())
coins = list(map(int, input().split()))

coins.sort()
target = 1

for coin in coins:
    if coin > target:
        print(target)
        exit()
    target += coin
