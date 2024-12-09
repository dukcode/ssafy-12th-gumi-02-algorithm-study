# 통계학
import sys
input = sys.stdin.readline

# 요구사항
# 산술평균, 중앙값, 최빈값, 범위 출력

# 오사오입 반올림 함수
def my_round(n):
    if n >= 0:
        if n - int(n) >= 0.5:
            return int(n) + 1
    else:
        if n - int(n) >= 0.5:
            return int(n)
    return int(n)

# 산술평균
# 소수점 이하 첫째자리 반올림
def average(data):
    result = round(sum(data) / len(data))
    return result

# 중앙값
# 홀수는 중앙값, 짝수는 중간값 2개의 평균
def middle(data):
    data = sorted(data)
    # 2로 나눴을때 나머지가 1 => 홀수
    if len(data) % 2 == 1:
        # 인덱스 0부터 시작하니까 이대로 하면됨
        result = data[(len(data) // 2)]
    else:
        result = my_round((data[(len(data) // 2)] + data[(len(data) // 2) - 1]) / 2)
    return result

# 최빈값
# 여러개 있을때 2번째로 작은 값
# 비교를 해야되는데 어떻게 하지

def many(data):
    count = [0] * (4001)
    minus_count = [0] * (4001)
    for i in data:
        if i >= 0:
            count[i] += 1
        else:
            minus_count[abs(i)] += 1
    
    max_many = max(max(count), max(minus_count))

    arr = []

    for i in range(4001):
        if count[i] == max_many:
            arr.append(i)
        if minus_count[i] == max_many:
            arr.append(-i)

    arr.sort()

    if len(arr) > 1:
        return arr[1]
    return arr[0]


# 범위
def my_range(data):
    # 1개면 0
    if len(data) == 1:
        result = 0
    # 2개 이상이면 각각의 최소 최대에 절대값을 걸고 뺀 결과에 절대값을 걸고 할당
    else:
        result = (max(data)) - (min(data))
    return result


data = []
num = int(input())
for _ in range(num):
    data.append(int(input()))

print(average(data))
print(middle(data))
print(many(data))
print(my_range(data))
