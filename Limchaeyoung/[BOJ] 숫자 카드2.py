# https://www.acmicpc.net/problem/10816
import collections
n = int(input())
mine = list(map(int, input().split()))
set_mine = set(mine)
cnt_mine = collections.Counter(mine)
m = int(input())
card = map(int, input().split())
for x in card:
    if x in set_mine:
        print(cnt_mine[x], end=' ')
    else:
        print("0", end=' ')