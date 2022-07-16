# https://www.acmicpc.net/problem/10815
n = int(input())
mine = set(map(int, input().split()))
m = int(input())
card = map(int, input().split())
for c in card:
    if c in mine:
        print("1" , end=' ')
    else:
        print("0", end=' ')
