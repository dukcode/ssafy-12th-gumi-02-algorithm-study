T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    result = [0] * N # 현주의 상자 처음 모습
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for a in range(L-1, R): # L-1번부터 R번까지(인덱스 순서)의 상자숫자를 i로 바꿈
            result[a] = i
    print(f'#{tc}', *result) # 현주의 최종 상자 모습이 출력됨
