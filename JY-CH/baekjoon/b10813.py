# 공 바꾸기

n, m = map(int, input().split())

answer = []
for i in range(1, n+1):
    answer.append(i)
# print(answer)
# answer2 = [1, 2, 3, 4, 5]

for l in range(m):
    j, k = map(int, input().split())
    for change in range(j, k):
        # answer[j-1] = answer2[k-1]
        # answer[k-1] = answer2[j-1]
        answer[j-1], answer[k-1] = answer[k-1], answer[j-1]
    # print(answer)

for i in range(n):                          # 이게 되네?
    print(answer[i], end=' ')

# 배열 교환 방법 몰라서 찾아봄.
# 첨에는 그냥 값 바꿔줄 생각하고 리스트를 하나 더짜서 넣는식으로 했는데
# 생각해보니까 3번째 변경이 성립이 안됨.

# 리스트 배열은 인덱스 찍고 바꿀수 있다.

# print 리스트를 풀 방법이 index 찍는거 뿐인데
# 내 돌대가리로는 답이 저거 밖에 없어서 찍었는데
# 이게 되네?
# 일단 다시 볼 문제 추가함.
