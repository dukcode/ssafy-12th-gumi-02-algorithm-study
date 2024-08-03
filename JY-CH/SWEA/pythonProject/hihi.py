# 'hello world!' 문자열 안에 'orl 이 있는지 검사!
# print('orl' in 'hello world!')
# A 안에 B가 포함되어 있으면 True, 아니라면 False를 반환
# def str_compare(A,B):
#     pass

# 회문검사 [::-1] 사용 X
# 반갈쳐서 끝값끼리 비교

from pprint import pprint

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

# 2차원 배열 형성
for a in range(n):
    sentence = [list(input().strip()) for _ in range(n)]
    # i랑 j를 통해 인덱스 설정
    # 행 순회 할건데 열 범위 설정을 했고
    for i in range(n):
        # 행을 순회 할건데
        for j in range(n // 2):
            # i열의 인덱스가 반대랑 다르면 걍 가고
            # 아니면 그 열 반환해라.
            if sentence[i][(n // 2) - 5 + j] != sentence[i][(n // 2) + 4 - j]:
                continue
            else:
                print(sentence[i])

# sentence[0][i : i + M]

# for i in range(n):
#     while 1:
#         if sentence[i] != sentence[n-i]:
#             continue
#         else :
#             print(sentence)