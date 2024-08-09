# 킹, 퀸, 룩, 비숍, 나이트, 폰

# 체스에 요구되는 말들을 리스트로 작성.
chess_list = [1, 1, 2, 2, 2, 8]

# 소유하고 있는 말들의 개수를 리스트로 작성.
# 리스트 형태로, 받는 값들 모두 정수 형태를 취하면서 띄워주세요.
own_list = list(map(int, input().split()))

# for문을 이용해 각 리스트의 index를 이용해 빼면 
# 요구되는 말의 개수를 맞추기 위해 필요한 or 불필요한 갯수 출력 가능
# 필요, 불필요한 갯수를 리스트로 작성.
# 1줄로 출력하기 위해 end=' ' 를 통해 공백을 두고 출력하게끔함
for i in range(len(chess_list)):
        need_list = chess_list[i] - own_list[i]
        print(need_list, end=' ')