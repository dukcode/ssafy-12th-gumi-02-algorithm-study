# 곱셈

def result(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = result(a, b // 2, c)
        return (half * half) % c
    else:  
        return (a * result(a, b - 1, c)) % c

# 입력 처리
a, b, c = map(int, input().split())
print(result(a, b, c))