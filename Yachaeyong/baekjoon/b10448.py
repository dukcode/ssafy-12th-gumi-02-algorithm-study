T = int(input())
for tc in range(T):
    K = int(input())
    N = 1000
    t = [n*(n+1)//2 for n in range(1, 46)]

    def f():
        for i in t:
            for j in t:
                for k in t:
                    temp = i + j + k
                    if temp == K:
                        return 1
        else:
            return 0

    print(f())