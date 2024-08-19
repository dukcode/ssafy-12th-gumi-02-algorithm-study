# https://www.acmicpc.net/problem/2309
def dfs(arr, h_sum=0, cnt=0):
    if cnt == 7:
        if h_sum == 100:
            for num in sorted(arr):
                print(num)
            exit()
        else:
            return

    for num in data:
        if num not in arr:
            arr.append(num)
            dfs(arr, h_sum+num, cnt+1)
            arr.pop()


data = [0] * 9
for i in range(9):
    data[i] = int(input())
dfs([])