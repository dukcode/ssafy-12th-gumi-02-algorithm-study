# 첫째 줄에 N (1 ≤ N ≤ 100)과 M (1 ≤ M ≤ 100)이 주어진다.

# 둘째 줄부터 M개의 줄에는 바구니의 순서를 역순으로 만드는 방법이 주어진다. 
# 방법은 i j로 나타내고, 왼쪽으로부터 i번째 바구니부터 j번째 바구니의 순서를 역순으로 만든다는 뜻이다. 
# (1 ≤ i ≤ j ≤ N)

# 도현이는 입력으로 주어진 순서대로 바구니의 순서를 바꾼다.
N, M = map(int, input().split())
basket = [x for x in range(1, N+1)]
for _ in range(M):
    i, j = map(int, input().split())
    basket[i-1:j] = reversed(basket[i-1:j])
print(*basket)

# 문제는 잘 풀었으나...요소를 리스트에 담아 그대로 출력하는 바람에...시간만 날림...