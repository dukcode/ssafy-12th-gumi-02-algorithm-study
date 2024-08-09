#영수증
#구매한 각 물건의 가격과 개수
#구매한 물건들의 총 금액을 보고, 구매한 물건의 가격과 개수로 계산한 
#총 금액이 영수증에 적힌 총 금액과 일치하는지 검사

X = int(input())
N = int(input())
price = 0

for i in range(N):
    a, b = map(int, input().split())
    price += (a * b)

if price == X:
    print('Yes')
else:
    print('No')