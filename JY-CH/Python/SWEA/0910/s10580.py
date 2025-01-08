# 전봇대

for tc in range(int(input())):
    n = int(input())
    word = [list(map(int, input().split())) for _ in range(n)]
    word.sort()

    cnt = 0
    for i in range(n):
        start, end = word[i]
        for j in range(i+1, n):
            if word[j][1] < end:
                cnt += 1

    print(f'#{tc+1} {cnt}')
