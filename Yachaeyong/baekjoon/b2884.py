H, M = map(int, input().split())

if (H >0) and (M < 45):
    M +=15
    H -= 1
    print(H, M)
elif (H == 0) and (M < 45):
    M += 15
    H = 23
    print(H, M)
else:
    M -=45
    print(H, M)