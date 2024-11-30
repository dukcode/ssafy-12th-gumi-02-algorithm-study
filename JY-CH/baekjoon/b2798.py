# 블랙 잭



card, target = map(int, input().split())
arr = list(map (int, input().split()))



data = []
for i in range(card - 2):
    for j in range(i + 1 , card - 1):
        for k in range(j + 1, card):
            if (arr[i] + arr[j] + arr[k]) <= target:
                data.append(arr[i] + arr[j] + arr[k])
            


print(max(data))