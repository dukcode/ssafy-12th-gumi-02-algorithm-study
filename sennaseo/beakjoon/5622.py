word = str(input())
count = 0
for x in word:
    if x in 'ABC':
        count += 3
    elif x in 'DEF':
        count += 4
    elif x in 'GHI':
        count += 5
    elif x in 'JKL':
        count += 6
    elif x in 'MNO':
        count += 7
    elif x in 'PQRS':
        count += 8
    elif x in 'TUV':
        count += 9
    elif x in 'WXYZ':
        count += 10
print(count)