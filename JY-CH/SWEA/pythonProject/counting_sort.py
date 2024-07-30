DATA = [0, 4, 1, 3, 1, 2, 4, 1]
COUNT = [0] * 5                         # DATA가 0~4까지의 정수


N = len(DATA)                           # DATA의 크기
TEMP - [0] * N                          # 정렬 결과 저장

# 1단계 : DATA 원소 별 개수 세기
for x in DATA:                          # DATA의 원소 x를 가져와서 COUNT[x]에 개수 기록
    COUNTS[x] += 1

# 2단계 : 각 숫자까지의 누적 개수 구하기
for i in range(1, 5):                   # COUNT[1] ~ COUNT[4]까지 누적개수
    COUNTS[i] : COUNTS[i-1] + COUNTS[i]

# 3단계 : DATA의 맨 뒤부터 TEMP에 자리 잡기
for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= -1               # 누적개수 1개 감소
    TEMP[COUNTS[DATA[i]] = DATA[i]

print(*TEMP)




# 1이상 10미만의 자연수 배열 정렬하기
arr = [7, 5, 8, 3, 7, 3, 1, 5, 9, 5, 1, 6, 9, 4]
# 1. 각 요소가 몇 개씩 나왔는지 세기
# 2. 각 요소의 개수를 누적합 구하기 >>> 각 요소가 들어갈 마지막 자리
# 3. 각 요소가 들어갈 자리에 요소를 넣어주기
# 필요한거
# 각 요소가 몇 개씩 나왔는지 세기 위한 배열
# >>> 크기가 요소 중 최대값보다 1 큰 배열
N = len(arr)
M = 10 # 요소 중 최대 값
count = [0] * M
sorted_arr = [0 * N]
# 1. 각 요소가 몇 개씩 나왔는지 세기
for i in range(N):
    # arr[i]가 몇 개 나왔는지 세야 합니다.
    count[arr[i]] += 1
# 2. 각 요소의 개수를 누적합 구하기.
#   앞의 요소 더하기 현재 요소의 값을 현재 요소의 자리에
for i in range(1,M):
    count[i] = count[i] + count[i-1]
    # count[i] += count[i-1]
# count : 각 요소의 개수 >>> 각요소의 마지막 위치
# 3. arr의 각 요소 위치에 맞게 빈배열에 넣어주기
for i  in range(N):
    # arr[i] >>> 5
    # count[5] >>> 5가 들어갈 위치
    count[arr[i]] -= 1
    sorted_arr[count[arr[i]]] = arr[i]

print((sorted_arr))

