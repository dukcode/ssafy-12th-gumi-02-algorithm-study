str1 = " " + input()
str2 = " " + input()
len1 = len(str1)
len2 = len(str2)
mat = [[""] * (len2) for _ in range(len1)]

for i1 in range(1, len1):
    for i2 in range(1, len2):
        if str1[i1] == str2[i2]:
            mat[i1][i2] = mat[i1 - 1][i2 - 1] + str1[i1]
        elif len(mat[i1][i2 - 1]) > len(mat[i1 - 1][i2]):
            mat[i1][i2] = mat[i1][i2 - 1]
        else:
            mat[i1][i2] = mat[i1 - 1][i2]

ans = mat[len1 - 1][len2 - 1]
print(len(ans))
if len(ans):
    print(ans)
