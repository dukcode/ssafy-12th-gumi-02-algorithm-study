S = str(input())
list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
result = [S.index(x) if x in S else -1 for x in list]
print(*result)