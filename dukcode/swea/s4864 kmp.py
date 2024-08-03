def kmp_search(sentence, target):
    n = len(sentence)
    m = len(target)

    ret = []
    partial_matches = get_partial_match(target)

    begin = 0
    matched = 0
    while begin <= n - m:
        if matched < m and sentence[begin + matched] == target[matched]:
            matched += 1
            if matched == m:
                ret.append(begin)
            continue

        if matched == 0:
            begin += 1
            continue

        begin += matched - partial_matches[matched - 1]
        matched = partial_matches[matched - 1]

    return ret


def get_partial_match(word):
    n = len(word)
    partial_matches = [0] * n

    begin = 1
    matched = 0

    while begin + matched < n:
        if word[begin + matched] == word[matched]:
            matched += 1
            partial_matches[begin + matched - 1] = matched
            continue

        if matched == 0:
            begin += 1
            continue

        begin += matched - partial_matches[matched - 1]
        matched = partial_matches[matched - 1]

    return partial_matches


t = int(input())
for tc in range(1, t + 1):
    target = input()
    sentence = input()

    ans = kmp_search(sentence, target)

    print(f"#{tc} {1 if len(ans) != 0 else 0}")
