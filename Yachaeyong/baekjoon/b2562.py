#최댓값
#9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 
#그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성

num = []
for _ in range(9):
    #input.split 남용 금지
    #이 경우는 for문으로 input만 써도 1줄씩 입력 받음
    num.append(int(input())) 

#max 함수로 최대값 구하기
print(max(num))
#인덱스는 0부터 세니까 몇번째 수인지 출력하기 위해 +1
print(num.index(max(num))+1)