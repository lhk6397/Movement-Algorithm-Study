# https://www.acmicpc.net/problem/11478
s = input()
data = set()
for x in range(1, len(s)):
    for y in range(0,len(s)+1):
        if y+x > len(s)+1:
            break
        data.add(s[y:y+x])
print(len(data))