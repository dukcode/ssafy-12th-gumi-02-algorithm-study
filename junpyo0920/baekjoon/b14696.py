for _ in range(int(input())):
    a = list(map(int, input().split()))[1:]
    b = list(map(int, input().split()))[1:]
    a_cnt = [0] * 4
    b_cnt = [0] * 4
    for i in range(1, 5):
        a_cnt[i-1] = a.count(i)
        b_cnt[i-1] = b.count(i)

    for i in reversed(range(4)):
        a_card = a_cnt[i]
        b_card = b_cnt[i]
        if a_card > b_card:
            print("A")
            break
        elif a_card < b_card:
            print("B")
            break
    else:
        print("D")
