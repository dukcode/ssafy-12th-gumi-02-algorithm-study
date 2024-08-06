# 최 댓 값
import pprint
from pprint import pprint


arr = [list(map(int, input().split())) for _ in range(9)]



max_value = 0
a = 0
b = 0
for i in range(9):
    for j in range(9):
        if max_value < arr[i][j]:
            max_value = arr[i][j]
            
        if max_value == arr[i][j]:
            a = i+1
            b = j+1







print(max_value)
print(a, b)

# pprint 써서 이쁘게 볼려고함.
# 커밋 수정좀