# 랜선 자르기
import sys
input = sys.stdin.readline


def search(data, num):
    start, end = 1, max(data)
    result = 0
    # 시작이 작거나 같으면 계속 돌린다
    # 만약 시작 포인트가 end를 넘어가면 while문 종료
    while start <= end:
        middle = (start + end) // 2
        cnt = 0
        for i in range(len(data)):
            cnt += (data[i] // middle)
        # 만약 카운트가 num과 같거나 크면?
        if cnt >= num:
            # '같거나'를 조건으로 달았으므로
            # 결과에 일단 중간값 할당
            result = middle
            # 그리고
            # 시작점 1 올리고 다시 시작
            start = middle + 1
            # cnt가 num보다 작으면
            # middle을 무조건 줄여야되니까
            # 1 까고 다시 돌림
        else:
            end = middle - 1
    return result



cable, num = map(int, input().split())
data = []
for i in range(cable):
    data.append(int(input()))
answer = search(data, num)
print(answer)




