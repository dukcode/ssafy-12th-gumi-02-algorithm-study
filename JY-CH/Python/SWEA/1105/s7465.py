# 창용 마을 무리의 개수

# 부모 노드 찾기
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b




t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())
    parent = [0] * (n + 1)

    for i in range(1, n + 1):
        parent[i] = i


    for _ in range(m):
        a, b = map(int, input().split())
        union_parent(parent, a, b)

    # 검증용 테이블
    check = [0] * (n + 1)
    for i in range(n + 1):
        # 해당값 인덱스를 1로 표기
        idx = find_parent(parent, i)
        check[idx] = 1

    cnt = 0
    # 1이면 카운트 올려서 그룹 부모 노드 세기
    for i in range(1, n + 1):
        if check[i] == 1:
            cnt += 1

    
    print(f'#{tc} {cnt}')
    

