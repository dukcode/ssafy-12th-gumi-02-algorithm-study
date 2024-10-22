# 좌표 압축
N = int(input())
X = list(map(int, input().split()))

new_x = sorted(list(set(X)))

x_dict = {}
for i in range(len(new_x)):
    x_dict[new_x[i]] = i

for x in X:
    print(x_dict[x], end=' ')
