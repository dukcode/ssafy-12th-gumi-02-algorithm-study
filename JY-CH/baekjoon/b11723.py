# 집합
import sys
input = sys.stdin.readline

# 공집합 (set) = S
S = set()

m = int(input())
for _ in range(m):
    order = input().strip().split()
    
    if order[0] == "add":
        x = int(order[1])
        S.add(x)

    elif order[0] == "remove":
        x = int(order[1])
        # 이 부분 S.discard(x)면 한줄로 정리가능
        if x in S:
            S.remove(x)

    elif order[0] == "check":
        x = int(order[1])
        print(1 if x in S else 0)

    elif order[0] == "toggle":
        x = int(order[1])
        if x in S:
            S.remove(x) 
        else:   
            S.add(x)

    elif order[0] == "all":
        S = set(range(1, 21))

    elif order[0] == "empty":
        S.clear() 