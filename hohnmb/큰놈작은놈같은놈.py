T = int(input().strip())
 
for t in range(1,T+1):
    numbers = list(map(int,input().split()))
    if numbers[0]>numbers[1]:
        print(f"#{t} >")
    if numbers[0]<numbers[1]:
        print(f"#{t} <")
    else:
        print(f"#{t} =")