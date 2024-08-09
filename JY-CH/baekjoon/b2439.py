# 별 찍기 2

# 시도횟수
t = int(input())


# 범위 설정
for tc in range(1, t+1):
    blank_num = t - tc
    print((' ' * blank_num) + ('*' * tc))

# 범위 아무 생각 없이 잡으면
# 별이 사라져요


# 근데 , 찍고 프린트 하면 출력 형식 오류가 나와요
# + 합시다 +