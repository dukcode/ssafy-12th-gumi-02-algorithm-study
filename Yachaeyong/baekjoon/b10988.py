#팰린드룸
#역순으로 반복해서 저장하고 비교하는게 포인트
#그냥 슬라이싱하면 더 간단함;
string = list(map(str, input()))
reverse = []

for i in range(len(string)-1, -1, -1):
    reverse.append(string[i])

if string == reverse:
    print('1')
else:
    print('0')
