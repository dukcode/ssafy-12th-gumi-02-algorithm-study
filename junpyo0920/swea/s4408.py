for tc in range(int(input())):
    num_of_students = int(input())
    moves = [sorted(list(map(int, input().split()))) for _ in range(num_of_students)]
    aisles = [0] * 200

    for move in moves:
        start_aisle = move[0] // 2 if move[0] % 2 else (move[0] - 1) // 2
        end_aisle = move[1] // 2 if move[1] % 2 else (move[1] - 1) // 2
        for idx in range(start_aisle, end_aisle + 1):
            aisles[idx] += 1
    
    print(f'#{tc + 1} {max(aisles)}')
