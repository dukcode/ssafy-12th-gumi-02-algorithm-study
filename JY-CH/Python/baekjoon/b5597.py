# 과제 안내신분..?

student_number = []

for i in range(28):
    a = int(input())
    student_number.append(a)

# print(student_number)
# print(sorted(student_number))

for i in range(1, 31):
    if i not in sorted(student_number):
        print(i)


# 함정이 있어유
# 첫 번째 for 문을 돌릴때는
# 어차피 입력값이 정해져있어서 28을 넣어도 0~27까지 28개가 들어가는데
# 막줄 i 넣고 돌릴때는 1~30의 값을 대조해보고 없으면 출력할거라
# 아무 생각없이 30넣어도 땡, 1넣고 돌리면 29까지 밖에 안가서 땡인데
# 입력시 출력 값은 동일하게 나옴. 단디 생각하자.