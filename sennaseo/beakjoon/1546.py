# 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 이 값은 1000보다 작거나 같다. 
# 둘째 줄에 세준이의 현재 성적이 주어진다. 
# 이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
# 첫째 줄에 새로운 평균을 출력한다. 
# 실제 정답과 출력값의 절대오차 또는 상대오차가 10-2 이하이면 정답이다.
# N = int(input())
# test_result = []
# test = list(map(int,input().split()))
# for y in test:
#     test_result.append(y)
# x = test_result.pop(test_result.index(max(test)))
# for i in range(len(test_result)): 
#     test_result[test_result[i]//x*100] = test_result.pop(i)
# print(test_result)

# 이번에도 빈리스트에 넣어서 최댓값을 꺼내보려 했지만
# 꺼낼 필요 없이 그냥 나눠주면 됐었다.
# 또한 리스트 컴프리헨션을 통해 더 간단하게 풀 수 있었다.

N = int(input())
test = list(map(int,input().split()))
max_test = max(test)
change_score = [(score/max_test)*100 for score in test]
average = sum(change_score) / N
print(f'{average:.2f}')