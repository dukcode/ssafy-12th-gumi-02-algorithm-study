for tc in range(int(input())):
    ans = -1
    input()
    nums = list(map(int, input().split()))
    while len(nums) > 1:
        new_num = nums.pop()
        for num in nums:
            mul = num * new_num
            str_mul = str(mul)

            for idx in range(len(str_mul)):
                if idx < len(str_mul) - 1:
                    if str_mul[idx] > str_mul[idx + 1]:
                        mul = -1
                        break
            
            ans = max(ans, mul)

    print(f'#{tc + 1} {ans}')
