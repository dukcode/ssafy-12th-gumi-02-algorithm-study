# 1이 될때까지

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())

    cnt = 0
    while N != 1:
        if N % K == 0 and K != 1:
            N = N//K
        elif K == 1:
            N = N - 1
        elif N % K != 0 or N < K:
            N = N-1
        cnt += 1

    print(f'#{tc} {cnt}')


# 문제 잘못 읽어서 1빼는걸 K로 쳐빼는 헛짓을 함.
# 입력 예시 하나는 금방 푸는데
# 몇몇개의 TC를 추가하면 추가적인 조건이 있어야만 올바르게 출력됨.
# 그냥 해보고 싶어서 해봄

### 입력값
# 4
# 25 5
# 5 1
# 30 6
# 101 10

### 출력값
#1 2
#2 4
#3 5
#4 3

# 채점이 없어서 틀렸을 확률 무조건 존재함!