# 회문
# from pprint import pprint

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(n)]
    # print()
    # pprint(arr)

    # n개 줄 검사
    for i in range(n):
        #n개 줄 m길이 검사용, j를 움직여서 확인할것.
        for j in range(n-m+1):
            # j는 움직일 수 있는선에서 움직일것.
            # m길이가 회문인지 확인하려면
            # 반가르고 앞뒤 인덱스 확인
            for k in range(m//2):
                if arr[i][j+k] != arr[i][j+m-1-k]:
                    break
            else :
                answer = ''.join(arr[i][j:j+m])

        # 2번은 위에서 아래로 검사하니까
        # 반전을 해보자


    arr2 = [[] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr2[i].append(arr[j][i])

    for i in range(n):
        #n개 줄 m길이 검사용, j를 움직여서 확인할것.
        for j in range(n-m+1):
            # j는 움직일 수 있는선에서 움직일것.
            # m길이가 회문인지 확인하려면
            # 반가르고 앞뒤 인덱스 확인
            for k in range(m//2):
                if arr2[i][j+k] != arr2[i][j+m-1-k]:
                    break
            else :
                answer = ''.join(arr2[i][j:j+m])



    print(f'#{tc} {answer}')