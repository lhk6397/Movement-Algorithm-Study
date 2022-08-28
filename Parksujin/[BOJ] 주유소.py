N = int(input())
len = list(map(int, input().split())) 
cost = list(map(int, input().split())) 

min_cost = cost[0] # 최소 비용 저장
ans = 0

for i in range(N-1):
  if cost[i] < min_cost: # 새로운 최소비용
    min_cost = cost[i] # 최소비용 갱신
  ans += (len[i] * min_cost) # 거리 * 비용
  
print(ans)
