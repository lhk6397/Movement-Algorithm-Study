# https://programmers.co.kr/learn/courses/30/lessons/42889
def solution(N, stages):
    fail = [0]*(N+1)
    fail_idx = [ x for x in range(1, N+1)]
    n = len(stages)
    stages.sort()
    for x in range(1, N+1):
        if n == 0:
            break
        fail[x] = stages.count(x)/n
        n -= stages.count(x)

    for x in range(1, N):
        for y in range(x+1, N+1):
            if fail[x] < fail[y]:
                fail[x], fail[y] = fail[y], fail[x]
                fail_idx[x-1], fail_idx[y-1] = fail_idx[y-1], fail_idx[x-1]
            elif fail[x] == fail[y]:
                if fail_idx[x-1] > fail_idx[y-1]:
                    fail_idx[x - 1], fail_idx[y - 1] = fail_idx[y - 1], fail_idx[x - 1]
    return fail_idx