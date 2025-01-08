# 문자열 반복



t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    s_list = list(s)
    # print(s_list)
    for i in range(len(s_list)):
        print(s_list[i] * r, end='')
    print()       # 줄바꿈을 생각도 못했습니다.


# r = int(r)
# # print(type(r))
# s_list = list(s)

# # print(s_list)

# for i in range(len(s_list)):
#     print(s_list[i] * r, end='')


# 출력시 
# 2
# 3 ABC
# AAABBBCCC5 /HTP
# /////HHHHHTTTTTPPPPP
# print() 없으면 이렇게 되요.
# 줄바꿈 용으로 넣어줘야됩니다.