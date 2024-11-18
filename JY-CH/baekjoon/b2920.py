#음계

trans = {
    1: 'c',
    2: 'd',
    3: 'e',
    4: 'f',
    5: 'g',
    6: 'a',
    7: 'b',
    8: 'C',
}

arr = []

def check(data, trans):
    for num in data:
        arr.append(trans[num])
    result = ''.join(arr)
    if result == 'cdefgabC':
        return 'ascending'
    elif result == 'Cbagfedc':
        return 'descending'
    else:
        return 'mixed'
    
data = list(map(int, input().split()))
answer = check(data, trans)
print(answer)

