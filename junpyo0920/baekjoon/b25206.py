grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F': 0.0
}

total_score = 0
cnt = 0

for _ in range(20):
    class_name, credit, grade = input().split()
    if grade == 'P':
        continue
    cnt += float(credit)
    total_score += float(credit) * grades[grade]

print(round(total_score / cnt, 6))