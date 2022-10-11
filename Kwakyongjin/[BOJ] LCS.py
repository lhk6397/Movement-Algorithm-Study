s1 = input()
s2 = input()
d = [0 for _ in range(len(s2))]

for i in range(len(s1)):
    cnt = 0
    for j in range(len(s2)):
        if cnt < d[j]:
            cnt = d[j]
        elif s1[i] == s2[j]:
            d[j] = cnt + 1
        
print(max(d))
