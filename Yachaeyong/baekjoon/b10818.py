# 최소, 최대
# N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

#min, max 함수 써서 간단하기 한데 3.8초 걸림
#시간복잡도 따질 단계는 아닌데 찝찝함

N = int(input())
num = list(map(int, input().split()))

print(f'{min(num)} {max(num)}')