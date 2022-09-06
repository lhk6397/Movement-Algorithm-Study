n = int(input())
table = []
for i in range(n):
    s, e = map(int, input().split())
    table.append((s, e))

table = sorted(table, key=lambda x:(x[1],x[0]))
start = table[0][1]
count = 1

for i in range(1, n):
    if table[i][0] >= start:
        count += 1
        start = table[i][1]
    
print(count)

