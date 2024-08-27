N, M = map(int, input().split())
numbers = [i for i in range(1, N+1)]
    
for i in range(M):
    j, k = map(int, input().split())
    temp = numbers[j-1:k]
    temp.reverse()
    numbers[j-1:k] = temp
    
for i in range(N):
    print(numbers[i], end=" ")