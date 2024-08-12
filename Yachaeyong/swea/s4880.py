def winner(i, j):
    if i == j:
        return i
    # 전체 범위 반씩 나눠서 진행
    # 승자의 인덱스 반환
    winner1 = winner(i, (i + j) // 2)
    winner2 = winner((i + j) // 2 + 1, j)

    # 무승부면 번호 낮은 사람이 승리
    if card[winner1] == card[winner2]:
        return winner1
    # 1>3
    if card[winner1] == 1:
        if card[winner2] == 3:
            return winner1
        else:
            return winner2
    # 2 > 1
    if card[winner1] == 2:
        if card[winner2] == 1:
            return winner1
        else:
            return winner2
    # 3 > 1
    if card[winner1] == 3:
        if card[winner2] == 2:
            return winner1
        else:
            return winner2


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(map(int, input().split()))

    print(f'#{tc} {winner(0, N - 1) + 1}')
