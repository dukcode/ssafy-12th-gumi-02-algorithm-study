# 5	[2, 1, 2, 6, 2, 4, 3, 3]  # [3,4,2,1,5]
# 4	[4,4,4,4,4]  # [4,1,2,3]


def solution(N, stages):
    counts = [0] * (max(max(stages), N) + 1)
    failures = [0] * (max(max(stages), N) + 1)

    for stage in stages:
        counts[stage] += 1

    for num in range(max(max(stages), N) + 1):
        jammed = counts[num]
        reached = 0

        for i in range(num, max(max(stages), N) + 1):
            reached += counts[i]

        failures[num] = tuple([0, num]) if reached == 0 else tuple([jammed / reached, num])

    failures.sort(key=lambda x: (-x[0], num))

    answer = []
    while len(answer) < N:
        stage = failures.pop(0)[1]

        if stage > N or stage == 0:
            continue
        answer.append(stage)

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
