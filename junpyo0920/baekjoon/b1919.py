str1 = input()
str2 = input()

counts1 = [0] * 26
counts2 = [0] * 26

for i in range(len(str1)):
    counts1[ord(str1[i]) - ord('a')] += 1

for i in range(len(str2)):
    counts2[ord(str2[i]) - ord('a')] += 1

ans = 0
for i in range(26):
    ans += counts1[i] - counts2[i] if counts1[i] > counts2[i] else counts2[i] - counts1[i]

print(ans)
