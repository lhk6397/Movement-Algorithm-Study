n = int(input())
arr = list(map(int, input().split()))
target = int(input())
result = 0

arr.sort()
st, ed = 0, n-1

while st < ed:
  if target > arr[st] + arr[ed]:
    st += 1
    continue
  elif target == arr[st] + arr[ed]:
    result += 1
  ed -= 1
print(result)