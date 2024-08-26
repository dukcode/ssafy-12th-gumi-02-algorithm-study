T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    result = -1 # 만약 Ai*Aj 중에서 단조 증가하는 수를 못찾으면 -1을 출력   
    for i in range(N-1):
        for j in range(i+1, N):
            multi = arr[i] * arr[j] # Ai * Aj하여 multi에 저장
            for k in range(len(str(multi)) - 1): # 숫자를 문자화 하여 (문자의 개수 -1) 을 range로 설정
                if str(multi)[k+1] < str(multi)[k]: # 각 위치의 숫자를 탐색하여 단조 증가하는 수가 아닐 때,
                    break                           # 즉시 반복을 종료하고 result로 -1을 출력
            else: 
                result = max(result, multi) # 숫자가 단조 증가하는 수일 때 result에 추가하고, 
                                                # result와 비교해서 더 큰수를 result에 저장 후 출력
    print(f'#{tc} {result}')

    # 이 문제는 문제를 해석하는데부터 어려웠다.
    # Ai와 Aj가 뭐를 의미하는지 헷갈렸다. 이해하는데 이틀걸림.
    # 문자화 시켜서 해결하는 방법을 아예 생각하지 못했다.
    # else가 탈출해서 break문을 만날시 for문 전의 항목부터 진행된다는 사실도 처음 알았다.