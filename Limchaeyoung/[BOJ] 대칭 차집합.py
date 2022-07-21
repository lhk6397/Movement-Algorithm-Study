# https://www.acmicpc.net/problem/1269
A, B = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
'''
a2 = a.copy()
b2 = b.copy()
for x in a:
    if x in b:
        a2.discard(x)
for x in b:
    if x in a:
        b2.discard(x)
print(len(a2)+len(b2))
'''
print(len(a-b)+len(b-a))