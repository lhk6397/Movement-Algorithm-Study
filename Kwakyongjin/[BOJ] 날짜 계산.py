import sys
input = sys.stdin.readline

t_e, t_s, t_m = map(int, input().split())
e, s, m, year = 1, 1, 1, 1

while True:
    if t_e == e and t_s == s and t_m == m:
        break
    e += 1
    s += 1
    m += 1
    year += 1

    if e >= 16:
        e -= 15
    if s >= 29:
        s -= 28
    if m >= 20:
        m -= 19

print(year)
