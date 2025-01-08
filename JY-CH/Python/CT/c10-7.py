# 팀 결성

# 루트 노드 찾는 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[a] = b
    else:
        parent[b] = a

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    cal, a, b = map(int, input().split())
    # 팀 합치기 연산일경우
    if cal == 0:
        union_parent(parent, a, b)
    # 같은 팀 여부확인
    # 루트 노드 체크
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('yse')
        else:
            print('no')

