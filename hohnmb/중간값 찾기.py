N = int(input())
lst = list(map(int, input().split())) 
lst.sort() 
print(lst[N//2])