# T = int(input())
# numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
# for tc in range(1, T + 1):
#     n, c = input().split()
#     examples = list(input().split())
#     result = []
#     for num in numbers:
#         for example in examples:
#             if example == num:
#                 result.append(example)
#     print(*result)
# 이렇게 푸는거 아닌거 같아서 다르게 풀려고 했는데 파훼법 못찾음

T = int(input())
numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for tc in range(1, T + 1):
    n, count = input().split()
    examples = list(input().split())

    for c in range(count):
        for num in numbers:
            if examples[c] == num:
                examples[c] = numbers.index(num)
                break

    examples.sort()

    for c in range(count):
        for num in numbers:
            if examples[c] == numbers.index(num):
                examples[c] = num
                break
    print(f"#{tc}", *examples)
