n, r, c = map(int, input().split())

def z_visit(n, r, c):
  if n == 1:
    a = str(r) + str(c)
    return int(a, 2)
  if r < 2**(n-1) and c < 2**(n-1):
    return z_visit(n-1, r, c)
  elif r < 2**(n-1) and c >= 2**(n-1):
    return 2**(2*n-2) + z_visit(n-1, r % 2**(n-1), c % 2**(n-1))
  elif r >= 2**(n-1) and c < 2**(n-1):
    return 2**(2*n-2) * 2 + z_visit(n-1, r % 2**(n-1), c % 2**(n-1))
  else:
    return 2**(2*n-2) * 3 + z_visit(n-1, r % 2**(n-1), c % 2**(n-1))

print(z_visit(n, r, c))