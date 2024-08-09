# 수열과 어떤 수(x)가 주어질 때, 수열 중 두 숫자의 합이 x가 되는 경우의 수를 구하는 문제

# 1트 -> 시간초과
# n = int(input()) # 수열의 크기
# nums = list(map(int, input().split())) # 수열
# target_num = int(input()) # 목표 값(x)

# ans = 0
# for i in range(n - 1):
#     for j in range(i, n):
#         if nums[i] + nums[j] == target_num:
#             ans += 1

# print(ans)

# 2트 (투 포인터 알고리즘)
n = int(input()) # 수열의 크기
nums = sorted(list(map(int, input().split()))) # 오름차순으로 정렬된 수열
target_num = int(input()) # 목표 값(x)

ans = 0
left = 0
right = n - 1
while left < right:
    if nums[left] + nums[right] == target_num: # left += 1로 해도 같음
        ans += 1
        right -= 1
    elif nums[left] + nums[right] < target_num: # 합의 크기가 커져야 함
        left += 1
    else: # nums[left] + nums[right]가 목표 값보다 큰 경우 / 합의 크기가 작아져야 함
        right -= 1

print(ans)

# input) 9 / 5 12 7 10 9 1 2 3 11 / 13
# nums = [1, 2, 3, 5, 7, 9, 10, 11, 12]
# 왼쪽 끝(1)과 오른쪽 끝(12)의 합(13)과 목표 값(13) 비교, 같으므로 오른쪽 끝 index 하나 줄임
# 왼쪽 끝(1)과 오른쪽 두 번째 끝(11)의 합(12)과 목표 값(13) 비교, 목표 값보다 작으므로 왼쪽 끝 index 하나 늘림
# 왼쪽 끝과 오른쪽 끝이 만날 때까지 반복