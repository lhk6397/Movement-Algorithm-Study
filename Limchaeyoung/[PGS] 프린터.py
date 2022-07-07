# https://school.programmers.co.kr/learn/courses/30/lessons/42587
from collections import deque
def solution(priorities, location):
    prior = deque()
    priorities = deque(priorities)
    idx = deque([x for x in range(len(priorities))])
    length = len(priorities)
    x = 0
    while True:
        if idx:
            if max(priorities) > priorities[x]:
                priorities.append(priorities.popleft())
                idx.append(idx.popleft())
            else:
                priorities.popleft()
                prior.append(idx.popleft())
        else:
            break
    return prior.index(location) + 1