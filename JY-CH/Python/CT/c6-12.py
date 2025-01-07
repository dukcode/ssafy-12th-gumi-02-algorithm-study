# 두 배열의 원소 교체

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# a 합 최대니까?
# a는 오름, b는 내림

a = sorted(a)
b = sorted(b, reverse=True)

# 내 풀이
for idx in range(k):
    if a[idx] < b[idx]:
        tmp = a[idx]
        a[idx] = b[idx]
        b[idx] = tmp
    else:
        break

# 책 풀이
# for idx in range(k):
#     if a[idx] < b[idx]:
#         a[idx], b[idx] = b[idx], a[idx]
#     else:
#         break


print(sum(a))

# 혹시 몰라서 시간복잡도 gpt한테 물어봤는데
# 둘다 시간복잡도가 O(K)이긴 하지만
# 내 풀이의 경우 할당연산 3회가 발생하고
# 책의 경우 내부적 할당연산 3회가 발생하나
# 최적화된 방식으로 처리된다고함