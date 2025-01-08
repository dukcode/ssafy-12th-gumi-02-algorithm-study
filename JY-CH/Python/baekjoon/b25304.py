# 영수증

# pay_all = int(input())
# var = int(input())

# for i in range(var):
#     money, cnt = map(int, input().split())
#     all_money = money[i]
#     print(all_money)


# 영수증에 적힌 총금액 x 입력 받는다
# 금액 비교할 변수 sum 0으로 초기화
x = int(input())
sum = 0

# 구매할 문건의 종류의 수 N만큼 반복, 물건의 가격a와 개수b 입력
# 금액을 비교할 변수 sum에 가격과 개수를 곱하여 더한다.
# 반복하명 총금액 출력 가능
for _ in range(int(input())):
    a, b = map(int, input().split())
    sum += a * b

# 영수증과 금액합이 맞다면 yes를 아니면 no를 출력
print("Yes") if sum == x else print("No")


# 분명 비슷하게 했을때 안됬는데 뭐가 문제였을까.. ㅠ
# 15분 이상 넘어가면 바로 답지보고 3일 내내 다시풀기