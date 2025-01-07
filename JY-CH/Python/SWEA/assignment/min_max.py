# 함수 정의

def length(num_list):
    cnt = 0
    for i in num_list:
        cnt += 1
    return cnt


def gap(num_list):

    max_value = num_list[0]
    min_value = num_list[0]

    for i in range(length(num_list)):
        if max_value < num_list[i]:
            max_value = num_list[i]

    for j in range(length(num_list)):
        if min_value > num_list[j]:
            min_value = num_list[j]

    return max_value - min_value

t = int(input())
for tc in range(1, t+1):
    num_list = list(map(int, input().split()))
    result = gap(num_list)
    print(f'#{tc} {result}')

# 우왕 길이 줬는데 길이 함수 만들어서 풀었당
# 함수 짜는거 재밌을지도?
