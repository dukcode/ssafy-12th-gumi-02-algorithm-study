# 별 찍기 7

n = int(input())

# for i in range(n):
#     blank = n - i - 1
#     print(' ' * blank  + '*' * ((i * 2) + 1) + ' ' * blank)

# for i in range(n-2, -1, -1):
#     blank = n - i - 1
#     print(' ' * blank  + '*' * ((i * 2) + 1) + ' ' * blank)

for i in range(n):
    blank = n - i - 1
    print(' ' * blank  + '*' * ((i * 2) + 1))

for i in range(n-2, -1, -1):
    blank = n - i - 1
    print(' ' * blank  + '*' * ((i * 2) + 1))


# 왜 뒤에 공백까지 넣었을까?