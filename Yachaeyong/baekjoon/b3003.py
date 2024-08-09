#킹, 퀸, 룩, 비숍, 나이트, 폰

piece = [1, 1, 2, 2, 2, 8]
find = list(map(int, input().split()))

for i in range(6):
    print(piece[i]-find[i], end=' ')

#num = []
# for i in range(len(find)):
#     if find[i] != piece[i]:
#         num.append(piece[i]-find[i])
#     else:
#         num.append(0)

# print(int(num.split()))

