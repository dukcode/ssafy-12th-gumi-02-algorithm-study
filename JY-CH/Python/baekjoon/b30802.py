# 웰컴 키트

# 펜은 딱맞게
# 같은 사이즈 t장 묶음, 티셔츠는 남아도 됨


# 23명
# 3 1 4 1 5 9
# 같은사이즈 t장 펜 p자루씩

# p자루를 명수에서 나눈다음 남는만큼 개별주문
# t셔츠는 인당 나누고 값이 있으면 1에서 시작 몫만큼 더하기


n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())

data = []
for i in size:
    if i % t == 0:
        data.append(i // t)
    else:
        data.append(i // t + 1)

set_order = n // p
order = n % p

print(sum(data))
print(set_order, order)