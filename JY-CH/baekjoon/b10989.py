# 수 정렬하기 3

# 입력값을 받자
n = int(input())
# 카운트 배열 받을거다. 마지막 범위엔 1을 추가하자.
# 안하면 마지막수가 짤린다.
# 입력값을 전부 받아야 하니까 마지막 범위에 1을 추가한다.
count = [0] * (n+1)
# for문을 통해 입력값 다 받고
for i in range(1, n+1):
    num = int(input())
    # count index에 입력 받은 숫자를 할당, 해당 인덱스에 +1
    count[num] += 1
print(count)

# 이러면 count는 인덱스에 해당 값의 갯수당 +1을 할당 받을것.
# 이제 이걸 꺼내보자

# n개까지 반복할거니까 +1
for i in range(n+1):
    # i를 반복할때 count[i]까지 돌면서
    for _ in range(count[i]):
        print(i)