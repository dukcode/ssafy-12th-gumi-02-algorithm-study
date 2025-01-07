# 시험 성적

# 입력값을 정수형으로 받을거에요
score = int(input())
if 90 <= score <= 100:
    print('A')
elif 80 <= score < 90:
    print('B')
elif 70 <= score < 80:
    print('C')
elif 60 <= score < 70:
    print('D')
else:
    print('F')

# 범위 설정후 남은 조건은 F밖에 없으므로 else에 넣었음.
# 80~89점의 경우 미만을 이용해서 수가 깔끔해 보이도록 만듬.

    