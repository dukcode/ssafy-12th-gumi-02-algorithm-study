# 문자열 뒤집기

S = input()

cnt10 = 0  # 0으로 바꾸는 횟수
cnt01 = 0  # 1로 바꾸는 횟수

if S[0] == '1':
    cnt10 += 1
else:
    cnt01 += 1

for i in range(len(S) - 1):
    if S[i] != S[i + 1]:
        if S[i + 1] == '1':  # 0->1이니까 1을 0으로 바꿔야함
            cnt10 += 1
        else:  # 1->0이니까 0을 1로 바꿔야함
            cnt01 += 1

print(min(cnt10, cnt01))
