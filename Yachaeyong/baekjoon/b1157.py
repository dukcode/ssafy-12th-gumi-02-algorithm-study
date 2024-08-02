# 단어 공부

#대문자 변환
words = input().upper()
word_list = list(set(words))
cnt = []

for word in word_list:
    count = words.count(word)
    cnt.append(count)

# cnt의 최대값 개수가 2개 이상인 경우
if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(word_list[cnt.index(max(cnt))])