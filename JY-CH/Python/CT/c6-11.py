# 성적이 낮은 순서로 학생 출력하기

n = int(input())

arr = []
for _ in range(n):
    student_score = input().split()
    # 정렬하기 위해선 점수를 숫자형으로 받기
    arr.append((student_score[0], int(student_score[1])))

# 정렬할건데 정렬의 기준은 점수로
arr = sorted(arr, key=lambda student_score: student_score[1])

for student_score in arr:
    print(student_score[0], end=' ')
