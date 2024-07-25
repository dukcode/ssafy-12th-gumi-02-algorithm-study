# 바구니 뒤집기
N, M = map(int, input().split())

box = [i for i in range(1, N+1)]

for _ in range(M):
    i, j = map(int, input().split())

    temp = box[i-1 : j] #1부터 시작해서 인덱스 맞춰주기
    temp.reverse() #원본 자체를 reverse
    box[i-1 : j] = temp #원본에 역순으로 바꾼거 대입

#그냥 box 프린트하면 리스트로 출력되므로
# * 달아서 언패킹 해줌.
print(*box, end=' ')

#reverse 함수와 .reverse() 차이점 공부하기
# for _ in range(M):
#     i, j = map(int, input().split())
#     # 부분 리스트를 추출하고 역순으로 뒤집음
#     sublist = box[i-1:j]
#     sublist.reverse()
#     # 역순으로 뒤집힌 부분 리스트를 다시 원본 리스트에 할당
#     box[i-1:j] = sublist
#---------------------------------
#     box[i-1:j] = reversed(box[i-1:j])








