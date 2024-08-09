# 그룹 단어 체커

N = int(input())
cnt = N

for i in range(N):
    word = input()
    
    #마지막 글자도 비교해야해서 -1 해줌
    for j in range(len(word)-1): 
        #현재 글자랑 다음 글자랑 같으면 패스
        if word[j] == word[j+1]:
            pass
        #다른데 현재 글자가 뒤에 있으면 그룹 단어 아니므로 -1하고 종료
        elif word[j] in word[j+1:]:
            cnt -= 1
            break
print(cnt)