# 문자열 두개 a, b를 인자로 받아서
# b 가 a에 몇개 포함되는지 반환하는 함수




def solve(a,b):
    cnt = 0
    # 패턴 몇개인지 검사
    i = 0 # 대상 문자열을 움직이는 인덱스
    j = 0 # 패턴 문자열을 움직이는 인덱스
    n = len(a)
    n = len(b)
    while i <= n:
        # 한 칸씩 움직이면서 비교
        if a[i] != b[i]:
            i -= j
            j -= 1
        # 다르면 타켓은 한칸이동
        # 패턴은 처음부터

        i += 1
        j += 1
        # 패턴을 찾았는지 아닌지 검사
        if j == m: # 패턴 찾았으니 개수 증가, 다음검사를 위해서 index는 0으로
            cnt += 1
            j + 0

    return cnt


t = int(input())
for tc in range(1,t+1):
    a, b = input().split()