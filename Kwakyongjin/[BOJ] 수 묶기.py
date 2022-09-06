import sys
input = sys.stdin.readline

posi_lst = []
zero_lst = []
nega_lst = []
count = 0

n = int(input().rstrip())
for _ in range(n):
    num = int(input().rstrip())

    if num > 1:
        posi_lst.append(num)
    
    elif num == 1:
        count += 1
    
    elif num == 0:
        zero_lst.append(num)
    
    else:
        nega_lst.append(num)
    

posi_lst.sort(reverse=True)
nega_lst.sort()
posi_len = len(posi_lst)
nega_len = len(nega_lst)

if posi_len % 2 == 0:
    for i in range(0, posi_len, 2):
        count += (posi_lst[i] * posi_lst[i+1])

else:
    count += posi_lst.pop()
    for i in range(0, posi_len - 1, 2):
        count += (posi_lst[i] * posi_lst[i+1])
    
if nega_len % 2 == 0:
    for i in range(0, nega_len, 2):
        count += (nega_lst[i] * nega_lst[i+1])
    
else:
    if zero_lst:
        nega_lst.pop()
        for i in range(0, nega_len - 1, 2):
            count += (nega_lst[i] * nega_lst[i+1])

    else:
        count += nega_lst.pop()
        for i in range(0, nega_len - 1, 2):
            count += (nega_lst[i] * nega_lst[i+1])

print(count)
