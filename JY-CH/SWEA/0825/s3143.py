# 가장 빠른 문자열 타이핑

T = int(input())
for tc in range (1, T+1):
    check, word = map(str, input().split())

    cnt = 0
    idx = 0
    while idx <= len(check) - len(word):
        if check[idx:idx+len(word)] == word:
            cnt += 1
            idx += len(word)
        else:
            idx += 1


    result = len(check) - (cnt * len(word)) + cnt
    print(f'#{tc} {result}')
        
