n = int(input())

d = [0] * (n+1)
squ = [i*i for i in range(1, 317)]

for i in range(1, n+1):
    s = []
    for j in squ:
        if j > i:
            break
        s.append(d[i-j])
    d[i] = min(s) + 1 

print(d[n])
