import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    a_len, b_len = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.sort()
    b.sort()

    tmp = 0
    b_index = 0

    for num in a:
        while b_index <= b_len - 1 and num > b[b_index]:
            b_index += 1
        tmp += b_index

    print(tmp)
