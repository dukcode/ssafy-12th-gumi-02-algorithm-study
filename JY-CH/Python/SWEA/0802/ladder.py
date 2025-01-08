# 사다리 타기 시작해서 끝이 2이면 true 아니면 false를 반환
# 사다리 타기 시작점을 인자로 받기

def solve(r ,c):
    # 한 칸, 한칸 이동하기 >> 제일 아래칸에 내려올때까지
    # 이동하는 방향을 저장하는 변수
    d = 0 # 0: 아래, 1: 왼쪽, 2: 오른쪽
    dr = [1, 0, 0]
    dc = [0, -1, 1]
    while r < 99:
        r += dr[d]
        c += dc[d]
        # 현재 진행방향이 아래쪽이면 왼쪽/오른쪽에 길이 있으면 이동
        # 현재 진향방향이 왼쪽/오른쪽이면 아래쪽에 길이 있으면 이동
        if d == 0: # 아래 방향으로 내려가고 있음
            if c > 0 and ladder[r][c-1] == 1:
                d = 1
            elif c < 99 and ladder[r][c+1] == 1:
                d = 2
        else: # 왼쪽 또는 오른쪽으로 이동중
            if r < 99 and ladder[r+1][c] == 1:
                d = 0
    
    # 맨 마지막 칸에 도달했더니 2가 있다면 목적지 발견
    if ladder[r][c] == 2:
        return True
    else:
        return False


for _ in range(10):
    tc = input()
    ladder = [list(map(int, input().split())) for _ in range(100) ]
    # 0 행에서 시작점 찾아서 solve() 실행하기
    # solve()의 결과가 true라면 시작점 열 번호 출력하고 끝내기
    for c in range(100):
        if ladder[0][c]:
            if solve(0,c):
                print(f'# {tc} {c}')
                break
