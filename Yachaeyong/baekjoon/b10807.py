#개수 세기
#총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.


N = int(input())  
numbers = list(map(int, input().split()))  
v = int(input())  

count = numbers.count(v)

print(count)
#-------------------------------#
# #원래 작성한 코드
# N = 11
# num = '1 4 1 2 4 2 4 2 3 4 4'
# v = 2

# num_list = []
# count = 0

# for i in num:
#     if i != ' ': #공백을 조건으로 추가하면 두자리 숫자를 인식 못 해서 실패
#         num_list.append(i) 

# for j in num_list:
#     if int(j) == v:
#         count += 1

# print(count)
