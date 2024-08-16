T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    game = list(map(int, input().split()))
    for a in range(M):
        i, j = map(int, input().split())
        if i+j <= len(game):
            for b in range(i-1, i+j-1):
                if game[b] != game[i-1]:
                    game[b] = game[i-1]
        else:
            for b in range(i-1, len(game)):
                if game[b] != game[i-1]:
                    game[b] = game[i-1]

    print(f'#{tc} {" ".join(str(x) for x in game)}')