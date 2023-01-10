import sys
from collections import deque
input = sys.stdin.readline

result = []
cnt = 0
tmp = 10e7
while cnt != tmp+1:
    lst = input().rstrip()
    
    lst_sp = lst.split()
    
    for i in lst_sp:
        if cnt != 0:
            i = ''.join(reversed(i)).lstrip('0')
            result.append(int(i))
        else:
            tmp = int(i)
        cnt += 1

result.sort()
print(*result, sep='\n')
