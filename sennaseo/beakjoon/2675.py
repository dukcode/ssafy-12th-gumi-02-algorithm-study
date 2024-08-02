T = int(input())
for _ in range(T):
    A, B = input().split()
    A = int(A)
    result = ''.join([i * A for i in B])
    print(result)

# join에 리스트 컴프리핸션을 쓸 수 있다는 사실을 몰라서
# 계속 변수를 만들어 진행해 보려 했다.

# T = int(input())
# for _ in range(T):
#     A, B = input().split()
#     for x in range(len(B)):
#         result = [B[x]]*int(A)
#         print(''.join(result), end='')