def solve(num=0, power=-1):
    if num == target:
        ret = ""
        for i in range(1, -power):
            ret += str(arr[i])
        return ret
    if power < -12:
        return "overflow"
    if num + (2 ** power) <= target:
        num += 2 ** power
        arr[-power] = 1
    return solve(num, power - 1)


for tc in range(int(input())):
    target = float(input())
    arr = [0] * 13
    ans = solve()
    print(f"#{tc + 1}", ans)