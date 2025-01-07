
number = int(input())
nums = list(map(int, input().split()))

max_grade = max(nums)
new_nums=[]
for num in nums:
    new_num = (num/max(nums))*100
    new_nums.append(new_num)

print(sum(new_nums)/number)

#
# nums = [40, 80, 60]
# max(nums)
# print((40/max(nums))*100)
#
#



