for tc in range(int(input())):
    n = int(input())
    counts = [0] * 5001
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b + 1):
            counts[i] += 1
    
    p = int(input())
    print(f'#{tc + 1}', end=' ')
    for i in range(p):
        c = int(input())
        print(counts[c], end=' ')
    print()
