import sys
input = sys.stdin.readline

sentence = input().rstrip()
key = input().rstrip()

cnt = 0
n = 0

while n <= len(sentence) - len(key):
    if sentence[n:n + len(key)] == key:
        cnt += 1
        n += len(key)
    
    else:
        n += 1
print(cnt)
