decode = {"ZRO" : 0, "ONE" : 1, "TWO" : 2, "THR" : 3, "FOR" : 4, "FIV" : 5, "SIX" : 6, "SVN" : 7, "EGT" : 8, "NIN" : 9}
encode = {0 : "ZRO", 1 : "ONE", 2 : "TWO", 3 : "THR", 4 : "FOR", 5 : "FIV", 6 : "SIX", 7 : "SVN", 8 : "EGT", 9 : "NIN"}


def GNS(string):

    atoi = []
    itoa = []

    # 문자를 숫자로 변환
    for i in range(N):
        atoi.append(decode[string[i]])
    # 변환한 숫자 리스트 정렬(버블 안됨 선택 정렬 필수)
    # 필수 아님 인덱스로 딕셔너리 키에 바로 접근하고
    # 2중 반복 돌리면 버블정렬도 가능
    # 선택 정렬
    for i in range(N-1):
        min_idx = i
        for j in range(i+1,N):
            if atoi[min_idx] > atoi[j]:
                min_idx = j
        atoi[i], atoi[min_idx] = atoi[min_idx], atoi[i]

    # 정렬한 리스트 글자로 변환
    for i in range(N):
        itoa.append(encode[atoi[i]])

    return itoa

T = int(input())
for tc in range(1, T+1):
    tc_num, len_tc = input().split()
    N = int(len_tc)
    string = list(input().split())
    
    result = GNS(string)

    print(f'#{tc}')
    print(*result)