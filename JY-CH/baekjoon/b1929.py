# 소수 구하기

# 에라스토테네시의 체 구현하기

import sys
input = sys.stdin.readline

def prime(m, n):
    # 0, 1은 기본적으로 소수가 아니므로 False를 2개 주고
    # 2부터 소수라 가정하고 배열 생성
    data = [False, False] + [True] * (n - 1)
    # 답을 담아낼 배열
    result = []

    # 2부터 돌린다
    for i in range(2, n+1):
        # 2는 True
        if data[i]:
            # 결과 배열에 집어넣는다.
            result.append(i)
            # i의 2배부터 n까지, i만큼 이동하면서 체크
            for j in range(i*2, n+1, i):
                # 싹다 소수에서 뺀다
                # i의 배수이기 때문에 소수가 될 수 없다
                data[j] = False
    return result 

m, n = map(int, input().split())
answer = prime(m,n)
for i in answer:
    # m보다 크면 출력
    # 만약에 prime 함수에서 m~n까지의 리스트를 만들면 시간초과 on
    if i >= m:
        print(i)