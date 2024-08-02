# 크로아티아 알파벳

change_alpha = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()


for alpha in change_alpha:
    word = word.replace(alpha, '_') #alpha가 입력에 있으면 _로 변환

print(len(word))