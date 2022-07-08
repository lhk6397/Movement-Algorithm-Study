from collections import Counter
n = int(input())
arr=[]
for _ in range(n):
  arr.append(int(input()))
sarr = sorted(arr)
counter = Counter(sarr)
print(round(sum(arr)/n))
print(sarr[n//2])
if n == 1:
  print(counter.most_common()[0][0])
else:    
  print(counter.most_common()[1][0] if counter.most_common()[0][1] == counter.most_common()[1][1] else counter.most_common()[0][0])
print(max(arr)-min(arr))
