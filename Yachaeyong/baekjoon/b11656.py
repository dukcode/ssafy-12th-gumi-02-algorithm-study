# 접미사 배열
S = input().strip()

s_list = []


for i in range(len(S)):
    s_list.append(S[i:])

s_list.sort()
for s in s_list:
    print(s)