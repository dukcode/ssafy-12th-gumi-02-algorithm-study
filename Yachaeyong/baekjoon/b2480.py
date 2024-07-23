A, B, C = map(int, input().split())

if A == B == C:
    money = 10000 + A * 1000

elif A == B or B == C or C == A:
    if A == B or A == C:
        money = 1000 + A * 100
    else:
        money = 1000 + B * 100
else:
    money = max(A, B, C) * 100

print(money)