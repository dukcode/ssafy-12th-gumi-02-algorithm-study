# 오븐 시계


# 정수로 받을거에요
# 시간과 분, 요리시간을 변수명으로 설정.
h, m = map(int, input().split())
cook_m = int(input())

# A, B, C 범위 설정 (의미가 있나?)
# 입력값이 주어지는 문제에서는 큰 의미가 없으나
# 만약 오전 오후와 시간 표기가 필요하다면 그때는 필요함.?
0 <= h <= 23
0 <= m <= 59
0 <= cook_m <= 1000

# 조건을 설정할건데

# 시간이 23시거나 23시전이고 조리시간과 분의 합이 60을 넘으면서
# 24시간에서 h를 뺀값이 조리시간과 분의 합을 60으로 나눈몫의 값보다 작거나 같으면
# 입력된 시간에 조리시간과 분의 합을 60으로 나눈 몫을 더하고 24시간을 뺀다음
# 분을 조리시간과 분의 합을 60으로 나눈 나머지를 출력한다.
if h <= 23 and ((cook_m + m) >= 60) and (24-h <= ((cook_m + m) // 60)):
    print((h + (((cook_m + m) // 60) - 24)), ((cook_m + m) % 60))
# 시간이 23시거나 23시전이고 조리시간과 분의 합이 60을 넘으면서
# 24시간에서 h를 뺀값이 조리시간과 분의 합을 60으로 나눈몫의 값보다 크면
# 입력된 시간에 조리시간과 분의 합을 60으로 나눈 몫을 더하고
# 분을 조리시간과 분의 합을 60으로 나눈 나머지를 출력한다.
elif h <= 23 and ((cook_m + m) >= 60) and (24-h > ((cook_m + m) // 60)):
    print((h + (((cook_m + m) // 60))), ((cook_m + m) % 60))
else :
    print(h, (cook_m + m))

# 내가 이겼다 이 ****
# 된거 같은데 틀리면 안되면 질문게시판으로 가보자
# 모든 경우에 코드가 적용이 되야 문제가 정답으로 찍힌다.
# 입력값 넣어서 출력 값 나왔다고 넣으면 틀린다.