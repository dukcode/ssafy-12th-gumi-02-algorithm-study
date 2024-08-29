def solve(num):
    global ans
    num = ord(num) - ord("A") + 10 if num in "ABCDEF" else int(num)
    ret = ""
    while num:
        ret = str(num % 2) + ret
        num //= 2
    while len(ret) < 4:
        ret = "0" + ret
    ans += ret


for tc in range(int(input())):
    size, hex_num = input().split()
    ans = ""
    for ch in hex_num:
        solve(ch)
    print(f"#{tc + 1} {ans}")