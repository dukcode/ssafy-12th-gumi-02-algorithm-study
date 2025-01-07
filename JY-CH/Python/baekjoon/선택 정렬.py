# 선택 정렬 재정리

# 예시
a = [12, 32, 56, 767, 9]
n = 5


# i는 갯수 -1의 범위로 돌린다.
# 만약 n을 넣고 돌릴경우 
# 아래 반복문에서 5,5가 index error 가 발생할것이다.
for i in range(n-1):
    min_idx = i
    # 내부 정렬용이다.
    # i를 이미 최소 값의 인덱스로 잡았기에 비교하고 더 낮은값이 있다면 정렬한다.
    for j in range(i+1, n):
        if a[min_idx] > a[j]:
            a[min_idx], a[j] = a[j], a[min_idx] 




print(a)
# 컷!