std = [i for i in range(1,31)]

for _ in range(28):
    num = int(input())
    std.remove(num)

print(min(std))
print(max(std))

# 총 인원 30명이니까 1부터 30까지 리스트를 만들고
# 과제 제출한 인풋 학생 을 num에 넣고
# 제출한 학생을 1~30까지 수에서 제거한다.
# 최소값과 최대값 출력