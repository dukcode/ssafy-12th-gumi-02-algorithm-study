a = input()
croatia_a = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia_a:
    a = a.replace(i, "*")

print(len(a))
