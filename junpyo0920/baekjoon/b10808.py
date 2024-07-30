# 문자열에 사용된 알파벳의 개수를 구하는 문제
# 처음에는 'a'부터 'z'까지 하나 하나 확인하려고 했음 -> 상당히 비효율적임
# 내장함수 ord()를 사용하면 ascii 코드를 알아낼 수 있음
# ord()로 'a'와 상대적인 위치를 알아내어 count 하는 것이 훨씬 효율적인 방법
word = input()
num_alpha = [0] * 26
for char in word:
    num_alpha[ord(char) - ord('a')] += 1
print(*num_alpha)