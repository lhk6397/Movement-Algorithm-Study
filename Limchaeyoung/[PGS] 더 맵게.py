# https://programmers.co.kr/learn/courses/30/lessons/42626
import heapq
def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + (second*2))
        cnt += 1
    return cnt