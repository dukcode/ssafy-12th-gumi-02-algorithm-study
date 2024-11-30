def number(a,b,c):
    a = int(a)
    b = int(b) 
    c = int(c)
    return a + b - c

# 더하기면 문자열로 앞뒤를 더해야됨
# 빼기면 정수형으로 바꿔서 앞뒤를 빼야됨

def string(a, b, c):
    a = str(a)
    b = str(b) 
    c = str(c)
    arr = [a, '+', b, '-', c]
    for idx in range(len(arr)):
        if arr[idx] == '+':
            new_value = (arr[idx - 1] + arr[idx + 1])
            arr[idx + 1] = new_value
        elif arr[idx] == '-':
            arr[idx - 1] = int(arr[idx - 1])
            arr[idx + 1] = int(arr[idx + 1])
            return arr[idx - 1] - arr[idx + 1]
   
        

a = input()
b = input()
c = input()

print(number(a, b, c))
print(string(a, b, c))