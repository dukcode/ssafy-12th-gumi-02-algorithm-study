TRUE = 1
FALSE = 0

t = int(input())
for tc in range(1, t + 1):
    target = input()
    sentence = input()

    def find(sentence, target):
        for i in range(len(sentence)):
            si = i
            find = True
            for ti in range(len(target)):
                if si >= len(sentence):
                    find = False
                    break

                if sentence[si] != target[ti]:
                    find = False
                    break

                si += 1

            if find:
                return TRUE

        return FALSE

    print(f"#{tc} {find(sentence, target)}")
