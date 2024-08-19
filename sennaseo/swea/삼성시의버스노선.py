T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A_list = []
    B_list = []
    for i in range(N):
        A, B = map(int, input().split())
        A_list.append(A)
        B_list.append(B)
    P = int(input())
    result = [0] * P
    for j in range(P):
        C = int(input())
        for i in range(N):
            for a in range(A_list[i], B_list[i]+1): # 정류장 거칠 때 마다
                if C == a:
                    result[j] += 1  # result의 정류장 인덱스를 +1
    print(f'#{tc}', *result)