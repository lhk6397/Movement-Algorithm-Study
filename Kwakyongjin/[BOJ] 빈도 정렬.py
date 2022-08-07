import sys
input = sys.stdin.readline

n, c = map(int,input().split())
lst = list(map(int, input().split()))
temp = dict()
for i in lst:
    if not i in temp:
        temp[i] = 1
    
    else:
        temp[i] += 1

temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)

for i in temp:
    for j in range(i[1]):
        print(i[0], end=' ')
