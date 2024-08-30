n = int(input())

end = 0
answer = 0

arr = []

for i in range(0,n):
    a, b = map(int, input().split())
    arr.append([a,b])

arr.sort(key=lambda x: (x[1], x[0]))

for newStart, newEnd in arr:
    if end <= newStart:
        answer += 1
        end = newEnd
print(answer)