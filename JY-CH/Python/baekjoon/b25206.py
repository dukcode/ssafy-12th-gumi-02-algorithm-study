# 너의 학점은

import sys
input = sys.stdin.readline

grade_to_score = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}

total_grade = 0
total_score = 0


for _ in range(20):
    name, score, grade = input().split()

    score = float(score)

    if grade == 'P':
        continue

    total_grade += score * grade_to_score[grade]
    total_score += score

# 전과목 p
if total_score == 0:
    result = 0
else:
    result = total_grade / total_score

# 파이썬 소수점 표기
print(f"{result:.6f}")


    