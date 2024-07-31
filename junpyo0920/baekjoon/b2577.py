from functools import reduce

# 세 개의 자연수 A, B, C가 주어졌을 때, A x B x C의 결과값에 0부터 9까지 각각의 숫자가 몇 번 사용되었는지 구하는 문제
# mul_abc = map(lambda a, b, c: a * b * c, *map(int, [input() for _ in range(3)]))

# reduce 함수를 사용하여, 주어진 숫자 a, b, c를 모두 곱함
# 곱한 값(int)을 str로 변환하여 iterable하게 만듬
# 각 문자를 다시 정수(int)로 변환하여 list에 담음
mul_abc = list(map(int, str(reduce(lambda a, b: a * b, map(int, [input() for _ in range(3)])))))

# 각 숫자의 빈도수를 저장할 리스트 생성
counts = [0] * 10

# mul_abc를 순회하며 각 숫자의 빈도수를 셈
for num in mul_abc:
    counts[num] += 1

# 0부터 9까지 빈도수를 출력
for count in counts:
    print(count)