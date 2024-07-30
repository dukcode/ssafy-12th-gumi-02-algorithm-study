# 0부터 9까지 숫자(숫자 카드)를 한 세트라고 할 때
# 숫자(방 번호)가 주어지면 총 몇 세트를 사용해야 하는지 구하는 문제
# 단, 6이나 9는 뒤집어서 사용 가능

room_num = list(map(int, input()))
# 방 번호의 각 숫자가 몇 번 들어가는지 저장하기 위한 리스트
counts = [0] * 10

# 각 숫자가 몇 번 들어가는지 체크
for num in room_num:
    counts[num] += 1

# 6과 9는 뒤집어서 사용할 수 있기 때문에 6이 사용된 수와 9가 사용된 수를 더하여 2로 나누어 반올림
counts[6] += counts.pop(9)
counts[6] = round(counts[6] / 2)

# counts에서 가장 큰 수가 사용된 카드 세트의 수
print(max(counts))
