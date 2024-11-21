grade_dic = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}

total = 0
point_total = 0
for _ in range(20):
    subject, point, grade = map(str, input().split())
    if grade != "P":
        total += float(point) * grade_dic[grade]
        point_total += float(point)

print(total / point_total)
