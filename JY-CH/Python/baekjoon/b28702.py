# FizzBuzz
import sys
input = sys.stdin.readline


check = ['Fizz', 'Buzz', 'FizzBuzz']
# 피즈버즈
# 3개씩 보는데 동시에 3개가 저 아래 체크를 완성할 수 없음.
# 무슨 짓을해도 n은 결국 동일한 값이 나옴
for i in range(3):
    x = input().strip()
    if x not in check:
        n = int(x) + (3 - i)

if n % 3 == 0 and n % 5 == 0:
    print('FizzBuzz')
elif n % 3 == 0:
    print('Fizz')
elif n % 5 == 0:
    print('Buzz')
else:
    print(n)