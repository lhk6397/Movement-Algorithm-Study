import sys
input = sys.stdin.readline

n = int(input().rstrip())
number = list(map(int, input().split()))
number.sort()

tmp = 1

for num in number:
    if tmp < num:
        break

    tmp += num

print(tmp)
