# 개수 세기

num = int(input())

a = list(map(int, input().split()))
    
need_num = int(input())

num_count = 0

for i in range(num):
    if  a[i] == need_num:
        num_count += 1
print(num_count)


## 승우가 도와줌
## 제정신이 아님 a 한줄인데 for 문으로 받은 정신병이 있어서 못품.
