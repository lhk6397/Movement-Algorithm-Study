import sys
input = sys.stdin.readline

sentence = list(map(int, input().rstrip()))

tmp = sentence[0]
count = 0

for i in range(1, len(sentence)):
    if tmp != sentence[i]:
        count += 1
        tmp = sentence[i]
    else:
        continue

if count % 2 == 0:
    print(count//2)

else:
    print((count + 1)//2)
