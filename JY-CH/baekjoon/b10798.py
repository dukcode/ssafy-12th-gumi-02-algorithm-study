# 세로 읽기

from pprint import pprint

# 내 풀이
#
# arr = [list(map(str, input())) for i in range(5)]
#
# # for i in range(5):
# #     if len(arr[i]) <
#
# for i in range(5):
#     while len(arr[i]) < 5:
#         arr[i].append('')
#
#
#
# for i in range(5):
#     for j in range(5):
#         print(arr[j][i], end='')
#
# 안되서 답지보러감.
# 이건 왜 안돼.?

# word라는 리스트를 생성하고 받은 요소들을 배열
words = []
for i in range(5):
  word = list(map(str, input()))
  words.append(word)


# 최대 15개의 글자
for i in range(15):
# 2차원배열 5열
  for j in range(5):
    # i가 words[j] 보다 작으면
    #
    if i < len(words[j]):

      print(words[j][i], end="")