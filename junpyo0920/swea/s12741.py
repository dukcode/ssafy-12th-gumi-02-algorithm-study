# string A + string B
# 시간 복잡도: O(N^2)
#   - O(len(A)) + O(len(B))로 완전히 새로운 string을 만듦
#   - Java의 literal string처럼 새로운 메모리에 복사해야 한다고 함

ans = ""

for tc in range(int(input())):
    a, b, c, d = map(int, input().split())
    start = a if a > c else c
    end = b if b < d else d
    ans += f"#{tc+1} {end - start if end > start else 0}\n"

print(ans)
