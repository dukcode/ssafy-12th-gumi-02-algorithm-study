#solved.ac
import sys
input = sys.stdin.readline

def my_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    return int(n)

n = int(input())
data = []
for i in range(n):
    data.append(int(input()))
data = sorted(data)


# 의견이 없으면 0
# 의견이 하나 이상 있으면 절사평균
# 절사 평균 3이상 부터 가능

if n == 0:
    print(0)
else:
    line = my_round(n * 0.15)
    if line > 0:
        data = data[line:-line]
    
    result = sum(data) / len(data)
    print(my_round(result))

# round는 오사오입 방식의 반올림 함수이다.
# 우리가 알고있는 보통의 반올림은 사사오입이며 이를 위해서는 
# 우리가 직접 만들어서 사용해야된다.

# sys.stdin.readlines는 한번에 모든줄을 읽고 리스트를 반환한다
# sys.stdin.readline는 한번에 한줄을 읽고 반환한다