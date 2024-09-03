def run_or_triplet(arr, idx):
    if idx < 3:
        return False
    for i in range(idx-1):
        for j in range(i+1, idx):
            for k in range(j+1, idx+1):
                if arr[i] == arr[j] == arr[k]:
                    return True
                tmp_arr = sorted([arr[i], arr[j], arr[k]])
                if tmp_arr[0] + 1 == tmp_arr[1] and tmp_arr[1] + 1 == tmp_arr[2]:
                    return True


for tc in range(int(input())):
    data = list(map(int, input().split()))
    player1 = [None] * 6
    player2 = [None] * 6

    print(f"#{tc+1}", end=" ")
    for i in range(12):
        idx = i // 2
        if i % 2 == 0:
            player1[idx] = data[i]
            if run_or_triplet(player1, idx):
                print(1)
                break
        else:
            player2[idx] = data[i]
            if run_or_triplet(player2, idx):
                print(2)
                break
    else:
        print(0)
