
# 증가할때 증가한 횟수를 세고, 만약에 다음 숫자가 현재 숫자보다 작으면, 1부터 다시 시작한다.
# 끝까지 진행됐을때 횟수를 따로 저장하고 증가한 횟수와 마지막에 저장한 횟수를 비교해서 큰 횟수에 해당하는 인덱스 값을 출력한다


T = int(input())

for tc in range(1,T+1):
    n = int(input())
    weight = list(map(int,input().split()))
    cnt = 1
    result = 0
    ans = []
    for i in range(1,n):
        if weight[i] < weight[i+1]:
            cnt += 1
            result = cnt
            ans.append(result)
        else: # 만약에 앞의 크기가 현재 개수보다 작으면 1로 초기화하고 다시 시작
            result = cnt
            ans.append(result)
            cnt = 1
    print(f'#{tc} {max(ans)}')








    