# 날짜 크기 비교 시 month*100 해보기 // 나중에 다시 풀어보기

import sys
input = sys.stdin.readline

n = int(input().rstrip())
table = []
for i in range(n):
    s_m, s_d, e_m, e_d = map(int, input().split())
    table.append([s_m*100 + s_d, e_m*100 + e_d])

table.sort(key=lambda x:(x[0],x[1]))
count = 0
end = 0
target = 301

while table:
    if target >= 1201 or target < table[0][0]:
        break

    for i in range(len(table)):
        if target >= table[0][0]:
            if end <= table[0][1]:
                end = table[0][1]
            
            table.remove(table[0])
        
        else:
            break
    
    target = end
    count += 1
        
if target < 1201:
    print(0)
else: 
    print(count)

