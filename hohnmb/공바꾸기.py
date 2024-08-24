n,m = map(int, input().split())
basket = [0]*n
temp = n+1

for x in range(n):
  basket[x] = x+1

for x in range(m):
  i,j = map(int, input().split())
  temp = basket[i-1]
  basket[i-1] = basket[j-1]
  basket[j-1] = temp

for x in range(n):
  print(basket[x], end=" ")