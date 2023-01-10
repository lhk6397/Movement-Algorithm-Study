n = int(input())

fibo = [0] * (1000001)
fibo[0] = 0
fibo[1] = 1
for i in range(2, abs(n) + 1):
    fibo[i] = (fibo[i-2] + fibo[i-1]) % 1000000000

if n == 0:
    print(n)
    print(n)

elif n < 0:
    if abs(n) % 2 == 0:
        print(-1)
        print(fibo[abs(n)])
    else:
        print(1)
        print(fibo[abs(n)])

else:
    print(1)
    print(fibo[n])
