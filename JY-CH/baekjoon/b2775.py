# 부녀회장이 될테야
import sys
input = sys.stdin.readline

def check(k, n):
    # 0층 카운트 해야됨
    apart = [[0] * (n + 1) for _ in range(k + 1)]
    for i in range(1, n + 1):
        # 0층은 i호에 i명 산다
        apart[0][i] = i

    for front in range(1, k + 1):
        for back in range(1, n + 1):
            # 1층부터 앞에 수를 계속 가져온다음 마지막 아래층 사람만 더하면 된다.
            apart[front][back] = apart[front - 1][back] + apart[front][back - 1]
    
    return apart[k][n]




t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())

    print(check(k,n))