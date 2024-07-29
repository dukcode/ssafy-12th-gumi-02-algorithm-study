# 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

numbers = []
for x in range(9):
    numbers.append(int(input()))

print(max(numbers))
print(numbers.index(max(numbers))+1)

# index함수를 몰라서 for문을 두번이상 돌려보며 복잡하게 문제를 풀었었다.
# index는 위치를 찾는 함수이다. 인덱스는 0부터 시작하니까 1을 더해주어야 한다.