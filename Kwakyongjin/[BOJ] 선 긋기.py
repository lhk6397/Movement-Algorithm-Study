import sys
input = sys.stdin.readline

n = int(input().rstrip())

table = list(list(map(int, input().split())) for _ in range(n))
table.sort()

start, end = table[0]
length = 0

for i in range(1, n):
    new_start, new_end = table[i]
    if end > new_start:
        end = max(end, new_end)
    else:
        length += (end - start)
        start, end = new_start, new_end
    
length += (end - start)
print(length)
