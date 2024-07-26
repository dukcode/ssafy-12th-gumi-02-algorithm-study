# 평균

N = int(input())
score = list(map(int, input().split()))

n = max(score) #최대값
new_score = [] #조작한 점수 리스트

for i in range(N):
    new_score.append(score[i]/n*100) 

#new_score의 요소들을 sum으로 다 더하기 가능. 
#sum(iterable요소)라서 쉽게 풀었음
print(sum(new_score) / N) 