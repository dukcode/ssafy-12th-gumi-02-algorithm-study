T=10
 
for t in range(1,T+1):
    tc = int(input())
 
    ladder_game = [list(map(int, input().split())) for _ in range(100)]
 
    destination = ladder_game[99].index(2)
 
    row = 99
    column = destination
 
    while row > 0:
        row -= 1
        while column < 99 and ladder_game[row][column + 1] == 1:
            column += 1
            ladder_game[row][column]=2
        while column > 0 and ladder_game[row][column - 1] == 1:
            column -= 1
            ladder_game[row][column]=2
     
    print(f'#{tc} {column}')