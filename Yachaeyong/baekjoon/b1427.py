# 소트인사이드

N = list(map(int, input().strip()))
N.sort(reverse=True)
ans = ''
for n in N:
    ans += str(n)
print(ans)