# 퍼펙트 셔플

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    word_list = list(map(str, input().split()))

    idx_even_word = []
    idx_odd_word = []
    new_word_list = []
    if N % 2 == 0:
        for i in range(N//2):
            idx_even_word.append(word_list[i])
            idx_odd_word.append(word_list[i+N//2])

    else:
        for i in range((N//2)):
            idx_even_word.append(word_list[i])
            idx_odd_word.append(word_list[i + (N // 2) + 1])
        if N % 2 == 1:
            idx_even_word.append(word_list[N//2])


    for i in range(N//2):
        new_word_list.append(idx_even_word[i])
        new_word_list.append(idx_odd_word[i])

    if N % 2 == 1:
        new_word_list.append(idx_even_word[-1])

    print(f'#{tc}', *new_word_list)