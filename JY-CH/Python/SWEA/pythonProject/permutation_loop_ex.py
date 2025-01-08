# 순열인데 반복문
# 이거 요소의 개수가 많아지거나 정해져 있지 않으면 안됩니다.
arr = ['A', 'B', 'C']
N = len(arr)
perm = [0] * N
for i in range(N):
    perm[0] = arr[i]
    for j in range[N]:
        if i != j:
            perm[1] = arr[j]
            for k in range(N):
                if k != i and k != j:
                perm[2] = arr[k]
                # print(perm)
                # run or triplet 검사
                if perm[0] == perm[1] and perm[0] == perm[2]:
                    return 'triplet'
                elif peorm[0] + 1 == perm[1] and perm[0] + 2 == perm[2]
                    return 'run!'
    return 'noting'