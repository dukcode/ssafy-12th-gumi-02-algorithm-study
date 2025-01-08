# 이진 탐색

def search(node):
    global num
    if node <= N:
        
        search(node * 2)
        arr[node] = num
        num += 1

        search(node * 2 + 1)
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [0] * (N+1)
    num = 1
    search(1)
    print(f'#{tc} {arr[1]} {arr[N//2]}')