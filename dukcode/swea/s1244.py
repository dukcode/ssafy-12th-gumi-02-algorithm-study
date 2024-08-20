# 최대 상금
t = int(input())


for c in range(1, t + 1):
    arr, n = input().split()
    arr = list(arr)
    n = int(n)
    vis = set()

    def swap(num_changed):

        if num_changed == n:
            return int("".join(arr))

        ret = -1
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                arr[i], arr[j] = arr[j], arr[i]

                if (num_changed, "".join(arr)) not in vis:
                    vis.add((num_changed, "".join(arr)))
                    ret = max(ret, swap(num_changed + 1))

                arr[i], arr[j] = arr[j], arr[i]

        return ret

    print(f"#{c} {swap(0)}")
