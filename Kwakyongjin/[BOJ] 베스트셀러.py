import sys
input = sys.stdin.readline

n = int(input())
books = {}

for i in range(n):
    book = input().rstrip()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

result = sorted(books.items(), key=lambda x:(-x[1],x[0]))
print(result[0][0])
