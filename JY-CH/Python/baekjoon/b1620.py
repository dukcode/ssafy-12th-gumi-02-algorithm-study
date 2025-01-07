# 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

n, m = map(int, input().split())


dict = {}
dict2 = {}
for i in range(1, n + 1):
    word = input().strip()
    dict[word] = i
    dict2[i] = word


for _ in range(m):
    sth = input().strip()
    # isdigit()
    # 문자열이 숫자로 구성되있는지 확인하는 메서드..
    if sth.isdigit():
        print(dict2[int(sth)])
    else:
        print(dict[sth])


# 리스트 넣고 터지길래 바로 딕셔너리로 돌렸는데
# isdigit은 생각도 못함..