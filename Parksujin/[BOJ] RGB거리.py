N = int(input())
cost = []
for i in range(N):
  cost.append(list(map(int, input().split())))

# 1번 집은 기본값, 2번 집부터 겹치지 않도록
# 2번 집 R을 골랐다면, 1번 집 G, B 중 최솟값. 총 비용을 cost에 저장
for j in range(1, len(cost)):
  cost[j][0] = cost[j][0] + min(cost[j-1][1], cost[j-1][2])
  cost[j][1] = cost[j][1] + min(cost[j-1][0], cost[j-1][2])
  cost[j][2] = cost[j][2] + min(cost[j-1][0], cost[j-1][1])
  
print(min(cost[N-1][0], cost[N-1][1], cost[N-1][2]))