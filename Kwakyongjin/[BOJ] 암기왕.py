import sys
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    note1 = set(map(int, input().split()))

    m = int(input().rstrip())
    note2 = list(map(int, input().split()))

    for num in note2:
        if num in note1:
            print(1)
        else:
            print(0)
