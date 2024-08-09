# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 
# 둘째 줄부터 N개의 줄에는 수가 주어진다. 
# 이 수는 10,000보다 작거나 같은 자연수이다.
# 첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
# 카운팅 정렬 이용

N = int(input())
arr = [int(input()) for _ in range(N)]
max_arr = max(arr)
min_arr = min(arr)

count = [0] * (max_arr + 1)

for i in range(N):
    count[arr[i]] += 1

for i in range(1, max_arr+1):
    count[i] += count[i-1]

temp = [0] * N
for i in range(N-1, -1, -1):
    count[arr[i]] -= 1
    temp[count[arr[i]]] = arr[i]

print(temp)

# 카운팅 정렬 로직과 코드 이해하고 외워서 썼는데 계속 안됐었는데,
# temp를 arr와 같은 크기로 만들었어야했는데,
# 처음에는 아예 빈 리스트로 만들어버리고, 급기야는 count와 같은 포멧으로 만들었다.