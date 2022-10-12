n = int(input())

fibo = [0] * (1000001)
fibo[1] = 1
fibo[2] = 2
for i in range(3, n+1):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 15746

print(fibo[n])
