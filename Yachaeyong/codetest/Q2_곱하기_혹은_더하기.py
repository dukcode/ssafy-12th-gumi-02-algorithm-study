'''
02984
567
'''
# 곱하기 혹은 더하기
S = input()
ans = int(S[0])

for i in range(1, len(S)):
    num = int(S[i])
    if ans <= 1 or num <= 1:
        ans += num
    else:
        ans *= num

print(ans)
