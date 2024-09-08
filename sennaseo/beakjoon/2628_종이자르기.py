def solve(arr):
    paper_cut = []

    for a in range(len(arr)-1):
        pcv = arr[a+1] - arr[a]
        paper_cut.append(pcv)
        return paper_cut


pr, pc = map(int, input().split())
N = int(input())
rc = []
cc = []
for _ in range(N):
    r, c = map(int, input().split())
    if r == 1:
        rc.append(c)
    if r == 0:
        cc.append(c)
rc.append(0)
cc.append(0)
rc.append(pr)
cc.append(pc)
rc.sort()
cc.sort()
prc = solve(rc)
pcc = solve(cc)

max_v = 0
for i in prc:
    for j in pcc:
        if i * j > max_v:
            max_v = i * j
print(max_v)
