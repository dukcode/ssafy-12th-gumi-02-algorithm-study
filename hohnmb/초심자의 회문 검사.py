T = int(input())

for tc in range(1,T+1):
    word = input()
    word_check = word[::-1]
    if word == word_check:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
    