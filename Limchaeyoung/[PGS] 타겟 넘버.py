# https://school.programmers.co.kr/learn/courses/30/lessons/1844
from collections import deque
def solution(numbers, target):
    cnt = 0
    k = 1
    queue = deque([(numbers[k-1], k)])
    queue.append((-numbers[k-1], k))
    while k <= len(numbers) and queue:
        n, k = queue.popleft()
        if k == len(numbers):
            if n == target:
                cnt += 1
            continue
        k += 1
        queue.append((n+numbers[k-1], k))
        queue.append((n-numbers[k-1], k))
    return cnt