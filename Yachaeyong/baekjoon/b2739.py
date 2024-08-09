#N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.

N = int(input())

for i in range(1,10):
    a = N * i
    print(f'{N} * {i} = {a}')