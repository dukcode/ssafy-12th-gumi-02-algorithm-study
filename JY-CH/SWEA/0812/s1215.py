def solve(arr, m):
    # 회문 카운팅용
    cnt = 0
    # 행 순회 드가즈아ㅏㅏ
    for i in range(n):
        # m만큼 문자열 회문인지 찾으러 드가즈아ㅏㅏ
        # m만큼 빼고 하나 더 해줘야 포함이 된다ㅏㅏ
        for j in range(n-m+1):
            # 크기 반갈, 앞뒤로 비교!
            for k in range(m//2):
                if arr[i][j+k] != arr[i][j+m-1-k]:
                    break
            else:
                cnt += 1

    #열 순회 드가즈아ㅏㅏㅏ
    for i in range(n):
        # m만큼 문자열 회문인지 찾으러 드가즈아ㅏㅏ
        # m만큼 빼고 하나 더 해줘야 포함이 된다ㅏㅏ
        for j in range(n-m+1):
            # 크기 반갈, 앞뒤로 비교!
            for k in range(m//2):
                if arr[j+k][i] != arr[j+m-1-k][i]:
                    break
            else:
                cnt += 1

    return cnt

T = 10
for tc in range(1, T+1):
    n = 8
    m = int(input())
    arr = [input() for _ in range(n)]
    result = solve(arr, m)
    print(f'#{tc} {result}')

