# 베스트셀러
import sys

input = sys.stdin.readline
# 딕셔너리 사용1
N = int(input())
sale_data = dict()
for _ in range(N):
    book_title = input().strip()
    if book_title in sale_data:
        sale_data[book_title] += 1
    else:
        sale_data[book_title] = 1

sort_book = sorted(sale_data.items(), key=lambda x:(-x[1], x[0]))
print(sort_book[0][0])

# # 딕셔너리 사용 2
# max_book = max(sale_data.values())
# book_list = []
# for key, value in sale_data.items():
#     if value == max_book:
#         book_list.append(key)
#
# book_list.sort()
# print(book_list[0])

# 리스트랑 set로만 푸는 방법
# books = [input().strip() for _ in range(N)]
# book_list = set()
# sale_data = []
#
# for book in books:
#     if book not in book_list:
#         sale_data.append((book, books.count(book)))
#         book_list.add(book)
#
# sale_data.sort(key=lambda x: (-x[1], x[0]))
# print(sale_data[0][0])
