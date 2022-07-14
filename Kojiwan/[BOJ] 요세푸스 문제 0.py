n, k = map(int, input().split())
cur = 0
arr = list(range(1, n + 1))
result = []
for _ in range(n):
  cur = ((cur + k - 1) % len(arr))
  result.append(arr[cur])
  del arr[cur]

result = [str(x) for x in result]
print('<'+ ', '.join(result) +'>')