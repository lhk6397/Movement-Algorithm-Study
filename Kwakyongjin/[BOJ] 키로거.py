import sys
input = sys.stdin.readline

t = int(input().rstrip())
cnt = 0
for _ in range(t):
    sentence = list(input().rstrip())
    left, right = [], []
    for i in sentence:
        if i == ">":
            if right:
                left.append(right.pop())
        elif i == "<":
            if left:
                right.append(left.pop())
        elif i=='-':
            if left:
                left.pop()
        else:
            left.append(i)
    
    print("".join(left)+"".join(reversed(right)))
