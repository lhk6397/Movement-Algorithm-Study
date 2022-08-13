# 계수정렬 알고리즘

import sys
input = sys.stdin.readline

n = int(input())
count = [0] * (10001)
for i in range(n):
    count[int(input())] += 1

for i in range(10001):
    if count[i] != 0:
        for j in range(count[i]):
            print(i)
