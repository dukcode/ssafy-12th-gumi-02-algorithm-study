# 첫째줄에 N과 X가 주어진다
# 둘째줄에 여러 숫자가 주어진다
# X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다.
N, X = map(int, input().split())
data = map(int, input().split())
for x in data:
    if x < X:
        print(x, end=" ")
# end=" "의 존재를 몰라서 또 새로운 변수 리스트 만들어서 집어넣고 출력했다
# end=" "를 사용하게 되면 답변들이 가로로 공백있게 출력된다.