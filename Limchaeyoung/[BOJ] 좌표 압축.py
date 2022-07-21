# https://www.acmicpc.net/problem/18870
import sys
input = sys.stdin.readline
n = int(input())
data = list(map(int, input().split()))
data2 = sorted(list(set(data)))
data_dic = { data2[x] : x for x in range(len(data2))}
for x in data:
    print(data_dic[x], end=' ')