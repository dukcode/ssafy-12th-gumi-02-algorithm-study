arr = [list(map(str,input())) for _ in range(5)]



for i in range(15):
    for j in range(5):
        if i < len(arr[j]):
            print(arr[j][i],end='')


# AABCDD
# afzz
# 09121
# a8EWg6
# P5h3kx

0 0 0 1 0 2 0 3 0 4
1 0 0 1 1 2 1 3 1 4
2 0 0 1 2 2 2 3 2 4
3 0 0 1 3 2 3 3 3 4
4 0 0 1 4 2 4 3 4 4
5 0 0 1 5 2 5 3 5 4