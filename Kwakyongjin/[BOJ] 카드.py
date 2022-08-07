import sys
input = sys.stdin.readline

n = int(input().rstrip())
dic = dict()
for i in range(n):
    num = int(input().rstrip())
    if not num in dic:
        dic[num] = 1

    else:
        dic[num] += 1
    
result = sorted(dic.items(), key=lambda x: (-x[1], x[0]))
print(result[0][0])
