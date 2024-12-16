# 곱셈

# 일일이 처리하면 시간 초과남
# 재귀를 이용, b가 0,1,2일때만 계산
# 미친 문제;;

def result(a, b, c):
    if b == 0:
        return 1
    elif b % 2 == 0:
        half = result(a, b // 2, c)
        return (half * half) % c
    else:  
        return (a * result(a, b - 1, c)) % c


a, b, c = map(int, input().split())
print(result(a, b, c))