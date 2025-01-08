# G.N.S


trans = {
    'ZRO': 0,
    'ONE': 1,
    'TWO': 2,
    'THR': 3,
    'FOR': 4,
    'FIV': 5,
    'SIX': 6,
    'SVN': 7,
    'EGT': 8,
    'NIN': 9,
}

def bubble(str_lst):
    for i in range(N-1):
        for j in range(N-1-i):
            if trans[str_lst[j]] > trans[str_lst[j+1]]:
                str_lst[j], str_lst[j+1] = str_lst[j+1], str_lst[j]


T = int(input())
for _ in range(1, T+1):
    tc, n = input().split()
    N = int(n)
    str_lst = input().split()
    result = bubble(str_lst)
    print(tc)
    print(*str_lst)


# 노트북이 아파해요
# 문자열에 숫자를 할당할 방법을 찾다가 딕셔너리 기억남.
# 근데 깡출력 하면 리스트 나와서 언패킹 해야됨.