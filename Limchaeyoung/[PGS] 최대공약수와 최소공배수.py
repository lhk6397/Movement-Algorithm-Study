def solution(n, m):
    a = min(n, m)
    b = max(n, m)
    return [gcd(a, b), lcm(a, b)]


def gcd(n, m):
    for x in range(n, 0, -1):
        if n % x == 0 and m % x == 0:
            return x


def lcm(n, m):
    return (n * m) // gcd(n, m)