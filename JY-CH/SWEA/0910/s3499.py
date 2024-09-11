# 퍼펙트 셔플
def num():
    return int(input())

def word():
    return list(map(str, input().split()))

def distribute():
    left = []
    right = []
    if n % 2 == 1:
        find_num = n//2 + 1
    else:
        find_num = n//2
    for idx in range(find_num):
        left.append(words[idx])
        if idx+find_num < n:
            right.append(words[idx+find_num])
    return [left, right]

def finish(word_list):
    ans = []
    if n % 2 == 1:
        find_num = n//2 + 1
    else:
        find_num = n//2
    for idx in range(find_num):
        for turn in range(2):
            if idx+1 > len(lst[turn]):
                continue
            ans.append(lst[turn][idx])
    return ans



for tc in range(num()):
    n = num()
    words = word()
    lst = distribute()
    print(f'#{tc+1}', *finish(lst))
