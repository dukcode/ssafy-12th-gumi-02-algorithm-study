T = int(input())
for _ in range(T):
    N = int(input())

    P = [0] * 101
    P[1] = P[2] = P[3] = 1
    P[4] = P[5] = 2
    P[6] = 3
    P[7] = 4
    P[8] = 5

    ans = 0
    if N >= 9:
        for i in range(9, N + 1):
            P[i] = P[i - 1] + P[i - 5]
    print(P[N])

# T = int(input())
# for _ in range(T):
#     N = int(input())
#
#     P = [0] * 101
#     P[1] = P[2] = P[3] = 1
#
#     ans = 0
#     if N >= 4:
#         for i in range(4, N + 1):
#             P[i] = P[i - 2] + P[i - 3]
#     print(P[N])
