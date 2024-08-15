# 요세푸스;;

from collections import deque

N, K = map(int, input().split())

live_list = list(range(1, N + 1))
death_list = []
q = deque(live_list)

while q:
	q.rotate( K * (-1) )
	H = q.pop()
	death_list.append(str(H))

print("<", ", ".join(death_list), ">", sep='')