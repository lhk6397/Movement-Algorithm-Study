N, M = list(map(int, input().split()))
ans = [] # 수열 저장

def dfs():
  if len(ans) == M: 
    print(' '.join(map(str, ans)))
    return
  
  for i in range(1, N+1): # 사전 순으로 증가하는 순서
    if i not in ans: # 중복 확인
      ans.append(i) 
      dfs() # [1] -> [1,2]
      ans.pop() # [1] -> [1,3]
      
dfs()
