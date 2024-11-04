#그룹 나누기

# 부모 찾는 함수
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
    # 부모 테이블
    parent = [0] * (n + 1)
    # 부모를 자기자신으로 초기화
    for i in range(1, n + 1):
        parent[i] = i
    
    data = list(map(int, input().split()))
    # 신청서 1개에 2개가 들어가니까 2곱하고, 2번 뛰어야됨
    for idx in range(0, m * 2, 2):
        # 부모 노드 체크
        union_parent(parent, data[idx], data[idx + 1])

    
    # 검증용 테이블
    check = [0] * (n + 1)
    for i in range(1, n + 1):
        # root가 있으면 그값에 해당하는 인덱스를 체크에 1로 표기
        root = find_parent(parent, i)
        check[root] = 1

    cnt = 0
    # 돌려서 1이면 카운트 올림
    for idx in range(n + 1):
        if check[idx] == 1:
            cnt += 1

    print(f'#{tc} {cnt}')


