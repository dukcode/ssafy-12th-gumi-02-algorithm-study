def enq(n):
    global last
    last += 1
    h[last] = n 
    c = last
    p = c//2
    while p >= 1 and h[p] > h[c]:
        h[p], h[c] = h[c], h[p]
        c = p
        p = c//2 

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))

    h = [0] * (N+1)
    last = 0

    for number in num:
        enq(number)


    sum_h = 0
    while N // 2 >= 1:
        N = N//2
        sum_h += h[N]

    print(f'#{tc} {sum_h}')
