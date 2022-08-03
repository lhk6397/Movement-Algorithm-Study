import sys
from itertools import combinations
input = sys.stdin.readline

S = list(map(int, input().split()))
while S[0] != 0:
    del S[0]
    new_S = list(combinations(S, 6))
    for i in new_S:
        print(*list(i), sep=' ')
    print()

    S = list(map(int,input().split()))
