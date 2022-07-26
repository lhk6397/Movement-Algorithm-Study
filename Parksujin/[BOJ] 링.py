N = int(input())
M = list(map(int, input().split()))

# 유클리드 호제법
def gcd(A, B):
  R = A % B
  if R != 0:
    return gcd(B, R)
  else:
    return B
  
for i in range(1, N):
  res = gcd(M[0], M[i])
  print('{0}/{1}'.format(M[0]//res, M[i]//res)) # 기약분수 형태로 출력
    