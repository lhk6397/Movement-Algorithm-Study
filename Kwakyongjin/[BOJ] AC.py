import sys
from collections import deque

t = int(input())
for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(input())
    num = sys.stdin.readline().rstrip()[1:-1].split(',')
    real_num = deque(num)
    rev = 0
    temp = True

    if n == 0:
        real_num = []

    for j in p:
        if j == 'R': # 뒤집기
            rev += 1
            
        else: # 버리기
            if len(real_num) < 1:
                temp = False
                print('error')
                break
            else:
                if rev % 2 == 0:
                     real_num.popleft() 
                else:
                    real_num.pop()

    if temp == True:
        if rev % 2 == 0:
            print("[" + ",".join(real_num) + "]")
        else:
            real_num.reverse()
            print("[" + ",".join(real_num) + "]")
