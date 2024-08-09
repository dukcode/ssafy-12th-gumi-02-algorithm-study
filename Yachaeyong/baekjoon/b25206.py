# 너의 평점은
grade = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

credit_sum = 0
total_grade = 0

for _ in range(20):
    lecture = list(input().split())
    if lecture[2] != 'P': # 등급이 P가 아니면
        credit_sum += float(lecture[1]) # 학점 총합
        grade_sum = float(lecture[1]) * grade[lecture[2]] # 학점*과목평점 합
        total_grade += grade_sum # 학점*평점 누적 합
print(format(total_grade / credit_sum, ".6f")) #전공평점 계산 ".6f"로 6자리까지만 출력
