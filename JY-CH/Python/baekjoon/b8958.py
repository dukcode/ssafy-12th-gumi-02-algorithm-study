# OX 퀴즈

def getscore(data):
    
    final = []
    score = 0
    for idx in range(len(data)):
        if data[idx] == 'O':
            score += 1
            final.append(score)
        else:
            score = 0
    
    return sum(final)

t = int(input())
for _ in range(t):
    ox = list(map(str, input()))
    answer = getscore(ox)

    print(answer)