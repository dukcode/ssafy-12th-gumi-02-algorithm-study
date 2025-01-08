# 암호 생성기
# 시도 횟수 10회
# 값 받고
for tc in range(1, 11):
    N = int(input())
    num_lst = list(map(int, input().split()))

# 5로 나눈 나머지에 1을 더해서 빼준다
#
    num = 0
    while True:
        num = (num % 5) + 1
        num_one = num_lst.pop(0)
        num_one -= num
        if num_one <= 0:
            break
        num_lst.append(num_one)
    num_lst.append(0)

    print(f"#{tc}", *num_lst)
