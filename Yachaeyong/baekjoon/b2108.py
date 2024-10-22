# 통계학
N = int(input())
num = [int(input()) for _ in range(N)]
num.sort()

# 산술평균
avg = round(sum(num) / N)
# 중간값
mid = num[N // 2]
# 최빈수
num_dict = dict()

for i in range(N):
    if num[i] not in num_dict:
        num_dict[num[i]] = 1
    else:
        num_dict[num[i]] += 1
        
mode_list = []
max_v = max(num_dict.values())

for key, value in num_dict.items():
    if value == max_v:
        mode_list.append(key)

mode_list.sort()

mode = 0
if len(mode_list) > 1:
    mode = mode_list[1]
else:
    mode = mode_list[0]

# 범위
extent = max(num) - min(num)

print(avg)
print(mid)
print(mode)
print(extent)
