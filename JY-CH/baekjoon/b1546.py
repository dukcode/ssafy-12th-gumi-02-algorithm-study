# 평균

number = int(input())
number_list = list(map(int, input().split()))
high_score = max(number_list)

for i in range(number):
    # number_list = list(map(int, input().split()))
    # print(number_list)
    # high_score = max(number_list)
    # number_list.remove(max(number_list))
    # # middle_score = max(number_list)
    # print(high_score)
    # # print(number_list)
    # print(sum(number_list[i] / high_score * 100)/number)
    number_list[i] = number_list[i] / high_score * 100

print(sum(number_list) / number)


# 제정신일때 풀자.
# 앞서 하도 줄바꿔서 입력 시켜놨더니 습관적으로 돌렸다가 런타임 에러 당했다.
# 문제 똑바로 읽어야된다. 한국말 어렵다.
# 평균을 구하는 방법은 똑같으나, 점수가 바뀐다.
# 바뀐 점수로 평균을 구하는 것이 핵심.