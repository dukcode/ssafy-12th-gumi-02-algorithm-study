# 상수

A, B = map(str, input().split())

A_re = A[2]+A[1]+A[0] #인덱싱으로 숫자 재조합
B_re = B[2]+B[1]+B[0]

if A_re > B_re:
    print(A_re)
else:
    print(B_re)