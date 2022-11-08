import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
trucks = deque(trucks)
finish = []
total_time = 0
weight = 0
current_brid = deque()

while len(finish) != n:
    for i in range(len(current_brid)):
        current_brid[i][1] += 1
    
    if current_brid:
        if current_brid[0][1] == w+1:
            fi_truck_weight, fi_w = current_brid.popleft()
            weight -= fi_truck_weight
            finish.append(fi_truck_weight)
            
    if trucks:
        if l >= weight + trucks[0]:
            truck = trucks.popleft()
            tmp = 1
            current_brid.append([truck, tmp])
            weight += truck

    total_time += 1

print(total_time)
