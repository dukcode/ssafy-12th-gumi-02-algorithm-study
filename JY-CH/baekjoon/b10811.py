# 바구니 뒤집기 (도현아 그만!!!)

n, m = map(int, input().split())

answer = []
for i in range(1, n+1):
    answer.append(i)
# print(answer)
# print(answer[1::-1])

for i in range(m):
    j, k = map(int, input().split())
    # answer = answer[:j-1] + list(reversed(answer[j-1:k]))
    # print(answer)
    answer = answer[:j-1] + list(reversed(answer[j-1:k])) + answer[k:]

print(*answer)
# for i in range(n):    
#     print(answer[i], end=' ')

# 답 낼때 앞문제에서 print for문 얻어걸린거 야무지게 돌렸습니다.
# 신기하게 배열을 더해도 list끼리 더해지네요.
# 역시 일단 저지르고 봐야 얻는게 있어.
# 대가리 밖자ㅏㅏㅏㅏㅏㅏ!