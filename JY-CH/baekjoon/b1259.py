# 팰린드롬수

# import sys
# input = sys.stdin.readline


# tc를 지정하지 않았다 -> while문으로 받아야된다

while True:
    data = list(input())

    # 0 들어오면그냥 종료
    if data[0] == '0':
        break

    
    for i in range(len(data) // 2):
        if data[i] != data[-(i + 1)]:
            print('no')
            break
    else:
        print('yes')
