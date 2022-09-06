import sys
input = sys.stdin.readline

n = int(input().rstrip())
count = 0
table = []

for _ in range(n):
    table.append(int(input().rstrip()))

tmp = table[-1]

for i in range(n-2, -1, -1):
    tmp -= 1
    if table[i] > tmp:
        count += table[i] - tmp
    
    else:
        tmp = table[i]
    
print(count)
