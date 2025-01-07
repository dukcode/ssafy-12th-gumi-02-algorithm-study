# 벌집


target = int(input())

# 반복문을 돌린다

# 조건에 부합하면 돈 횟수 프린트


def find(target):
    cnt = 0
    num = 1
    while True:
        # 1회 돌때마다 카운트 1개
        cnt += 1
        # 카운트가 1이면
        # num == 1
        # target 보다 num이 같거나 작으면
        # 멈춘다
        num += (3 * 2 * (cnt - 1))
        # print(num)
        if target <= num:
            return cnt
        


answer = find(target)

print(answer)

