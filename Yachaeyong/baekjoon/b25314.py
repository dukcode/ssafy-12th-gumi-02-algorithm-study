#N바이트 정수까지 저장할 수 있다고 생각하는 정수 자료형의 이름 출력하기

N = int(input())

for i in range(4, N+1, 4):
    length = i//4 * 'long '
print(f'{length}int')