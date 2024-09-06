# n = int(input())
# data = sorted(list(map(int, input().split())))
# print(sum([x * (n - idx) for idx, x in enumerate(data)]))

# 순서가 앞에 있을 수록 해당 사람의 소요시간이 총 소요시간에 더 많이 더해짐
# 따라서 오름차순으로 정렬해야 총 소요시간이 가장 작아짐
n = int(input())
data = list(map(int, input().split()))
data.sort()
ans = 0
for i in range(n):
    for j in range(i+1):
        ans += data[j]
print(ans)
