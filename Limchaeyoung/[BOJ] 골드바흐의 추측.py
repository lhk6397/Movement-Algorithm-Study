# https://www.acmicpc.net/problem/6588
import sys
input = sys.stdin.readline
check_prime = [True] * 1000001
for i in range(2, 1001):
    if check_prime[i]:
        for j in range(i+i, 1000001, i):
            check_prime[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, n+1, 2):
        if check_prime[i] and check_prime[n - i]:
            print(n, "=", i, "+", n - i)
            break

