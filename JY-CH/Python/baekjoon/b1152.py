# 단어의 개수


sen = input()

# 내 풀이

# sen_list = list(sen.split(' '))

# if '' in sen_list:
#     print(len(sen_list) - sen_list.count(''))
# else:
#     print(len(sen_list))

# 야매입니다.
# 다른 케이스가 생기면 적용이 안되요. 쓰레기에요.


# 정석

sen_list = list(sen.split())

print(len(sen_list))



# 리스트 공백으로 나눠서 len만 쓰면 되는데?
# 모르겠어서 답지 볼려고 했는데 번떡이는 split
# 등신짓 했음.
