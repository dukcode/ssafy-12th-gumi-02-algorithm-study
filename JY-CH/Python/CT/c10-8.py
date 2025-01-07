# 도시 분할 계획

# 루트 노드 찾기
# def find_parent(parent, x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent, parent[x])
#     return parent[x]

# # 합치기
# def union_parent(parent, a, b):
#     a = find_parent(parent, a)
#     b = find_parent(parent, b)
#     if a < b:
#         parent[a] = b
#     else:
#         parent[b] = a

# house, road = map(int, input().split())
# parent = [0] * (house + 1)


# for i in range(1, house + 1):
#     parent[i] = i

# for _ in range(road):
#     a, b, cost = map(int, input().split)
# # cost순로 정렬은 해야되는데 이걸 어케하지?
#     cost, a, b ?

# -------------여기 뒤로 손 못댐-------------------

# 루트 노드 찾기
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


house, road = map(int, input().split())
parent = [0] * (house + 1)

## 모든 간선을 담을 리스트, 최종 비용을 담을 변수
edges = []
result = 0


for i in range(1, house + 1):
    parent[i] = i

for _ in range(road):
    a, b, cost = map(int, input().split)
    # 간선을 담을 리스트에 cost를 첫번째 원소로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로정렬
edges.sort()
# 비용 제일 큰놈 킵할 변수
last = 0

for edge in edges:
    cost, a, b = edge

    # 사이클 유무 확인, 없을때만 집합 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        # 결과 값에 비용을 합치고?
        result += cost
        # 비용순으로 정렬했으니까 마지막에 들어오는놈이 젤 비싼 비용이라서?
        last = cost

# 이렇게하면 자연스럽게 가장 비용이 큰 간선을 뺄 수 있다!
print(result - cost)