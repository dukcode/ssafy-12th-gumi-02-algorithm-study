## 입력 받은 값을 나눠줌
A, B, C=input().split()
## 문자열을 정수로 바꿔줌
A = int(A)
B = int(B)
C = int(C)
## 출력
print((A+B)%C)
print(((A%C)+(B%C))%C)
print((A*B)%C)
print(((A%C)*(B%C))%C)


