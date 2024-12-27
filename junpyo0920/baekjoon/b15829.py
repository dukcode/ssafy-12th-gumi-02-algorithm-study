M = 1234567891
l = int(input())
word = input()

result = 0
for i in range(l):
    result += ((ord(word[i]) - ord('a') + 1) * (31 ** i)) % M

print(result % M)