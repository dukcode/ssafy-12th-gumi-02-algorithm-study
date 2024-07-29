# 다이얼
# dial.index()와 enumerate로 구하는 방법 2개

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

grandma = input()
time = 0

for i in grandma:
    for idx, di in enumerate(dial): # 0,'ABC' 
        if i in di:
            time += (idx + 3) # 2는 3초걸리므로 인덱스만큼 더하기

print(time)