def solve(N):
    if N < 20:
        return 1 # 20보다 작아지면 10이므로 케이스가 1개밖에 안생긴다
    else:
        return solve(N-20) * 2 + solve(N-10) 
        # 20일때의 패턴이 계속 반복되므로 10의 짝수배수를 맞춰주기 위해 -10한 재귀함수를 사용하고
        # 20일때 하나씩 빼주며 20일때의 패턴의 개수를 센다.
        # -10한 재귀함수를 통해서 10일때의 패턴(1개)를 더해준다.


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f'#{tc} {solve(N)}')