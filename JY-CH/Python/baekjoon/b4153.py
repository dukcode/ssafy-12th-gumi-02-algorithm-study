# 직각 삼각형

def check(x, y, z):
    
    if max(x, y, z) == z:
        if (x ** 2) + (y ** 2) == (z ** 2):
            return 'right'
        else:
            return 'wrong'
        
    if max(x, y, z) == y:
        if (x ** 2) + (z ** 2) == (y ** 2):
            return 'right'
        else:
            return 'wrong'
        
    if max(x, y, z) == x:
        if (z ** 2) + (y ** 2) == (x ** 2):
            return 'right'
        else:
            return 'wrong'
    
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
    result = check(a, b, c)
    print(result)

# a b c가 0 이 아니면 함수에 넣는걸로 해서 계속 틀렸는데
# 그냥 a b c 가 0 이면 break를 했어야됬다;;