T = int(input())

for _ in range(1,T+1):
    tcm = int(input())
    trl = list(map(int,input().split()))
    # 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3

# 점수가 0부터 100이니까 100까지의 빈 리스트를 만든다.
    empty_list = [0] * 101
    # 0, 0, 2, 1, 1, 2, 0, 1, 4, 1, 1
# 빈 리스트에 중복된 숫자만큼 1 추가하기
    for k in trl:
        empty_list[k] += 1
    max_idx = 0

    # # i = 0, 0, 2, 1, 1, 2, 0, 1, 4, 1, 1
    # for i in empty_list:
    #     # 0 > 0 0 > 2 1 > 2 1 > 2 2 > 2 0 > 2 1 > 2 4 > 2 4 1 > 4 1 > 4 // 최빈횟수 4다. 
    #     if i > max_idx:
    #         max_idx = i
    # # 그니까 빈도횟수저장 최빈횟수인 숫자(인덱스)를 찾아줘
    # print(f'#{tcm} {empty_list.index(max_idx)}')

    # # i = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    for i in range(len(empty_list)):
        # 이 숫자가 얼마나 등장했어? 를 비교하고 있음
        # 0의 빈도횟수가 최대 빈도횟수(0) 숫자보다 크니? 0
        # 1의 빈도횟수가 최대 빈도횟수(0) 숫자보다 크니? 갱신x
        # 2의 빈도횟수(2)가 최대 빈도횟수 숫자(0)보다 크니? 갱신o -> 최대 빈도횟수 2
        # ...
        # 최대 빈도횟수인 숫자 출력.
        if empty_list[i] > empty_list[max_idx]:
            max_idx = i
    # 그니까 최빈수를 출력해줘.
    print(f'{tcm} {empty_list[max_idx]}')
            

# 단, 카운트 된 값이 같은 인덱스가 있을경우 값이 높은의 인덱스 값 출력한다




