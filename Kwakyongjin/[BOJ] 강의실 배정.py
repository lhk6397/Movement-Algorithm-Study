import heapq
import sys
input = sys.stdin.readline

n = int(input().rstrip())

table = [list(map(int, input().split())) for _ in range(n)]
table.sort()

table_queue = []
heapq.heappush(table_queue, table[0][1])

for i in range(1, n):
    if table[i][0] < table_queue[0]:
        heapq.heappush(table_queue, table[i][1])
    
    else:
        heapq.heappop(table_queue)
        heapq.heappush(table_queue, table[i][1])
    
print(len(table_queue))
