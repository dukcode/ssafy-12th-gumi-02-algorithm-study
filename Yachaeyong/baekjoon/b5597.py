#5597_과제 안 내신 분?

student = [i for i in range(1,31)] #리스트 컴프리헨션

for _ in range(28): # 제출한 28명 번호 받기
    submit = int(input())
    student.remove(submit) #제출한 번호 지우기 

print(min(student))
print(max(student))

# submit_student = []
# nonsubmit_student = []

# for _ in range(1,29):
#     submit_student.append(int(input()))

# submit_student.sort()

# for i in submit_student:
#     if submit_student[i]+1 != submit_student[i+1]:
#         nonsubmit_student.append(submit_student[i]+1)

# nonsubmit_student.sort()

# print(nonsubmit_student[0])
# print(nonsubmit_student[1])