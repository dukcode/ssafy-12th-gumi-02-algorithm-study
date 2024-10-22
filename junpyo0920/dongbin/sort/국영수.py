n = int(input())
score_data = [None] * n

for i in range(n):
    name, kor, eng, math = input().split()
    score_data[i] = (-int(kor), int(eng), -int(math), name)

score_data.sort()

for arr in score_data:
    print(arr[3])
