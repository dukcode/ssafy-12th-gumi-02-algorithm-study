# 구구단

# 정수형으로 입력값 받을거에요
number = int(input())


# n = 0 부터 시작
# n이 8보다 작거나 같아질때까지
# n을 1을 더해서
# 입력값이랑 곱한다음 출력
n = 0
while n <= 8:
    n += 1
    n * number
    print(f'{number} * {n} = {n * number}')
    continue