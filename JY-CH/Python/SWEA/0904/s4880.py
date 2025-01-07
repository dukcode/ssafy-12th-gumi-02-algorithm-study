# 토너먼트 카드게임
# 1 = 가위, 2 = 바위, 3 = 보
def winner(i, j):
    if i == j:
        return i
    # 반갈치고 진행
    # 1그룹, 2그룹의 승자 받아와야됨
    # 1그룹 끝내고
    # 2그룹 끝낸다음 매칭
    winner1 = winner(i, (i+j) // 2)
    winner2 = winner((i+j) // 2 + 1, j)

    # 같으면 앞에놈 부터
    if p_card[winner1] == p_card[winner2]:
        return winner1

    # 가위로 이길때
    if p_card[winner1] == 1:
        if p_card[winner2] == 3:
            return winner1
        else:
            return winner2

    # 바위로 이길때
    if p_card[winner1] == 2:
        if p_card[winner2] == 1:
            return winner1
        else:
            return winner2

    # 보로 이길때
    if p_card[winner1] == 3:
        if p_card[winner2] == 2:
            return winner1
        else:
            return winner2


for tc in range(int(input())):
    player = int(input())
    p_card = list(map(int, input().split()))

    # 승자의 경우 index를 가져온거라 +1
    print(f'#{tc+1} {winner(0, player-1) + 1}')





