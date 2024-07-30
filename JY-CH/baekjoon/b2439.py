# 별 찍기 2

# 시도횟수
t = int(input())


# 범위 설정
for tc in range(1, t+1):
    blank_num = t + 1 - tc
    print(' ' * blank_num, '*' * tc)

# 범위 아무 생각 없이 잡으면
# 별이 사라져요
# 이거 먼저하고 long 출력 풀었으면 풀었다 ㄹㅇ