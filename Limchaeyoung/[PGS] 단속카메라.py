# https://school.programmers.co.kr/learn/courses/30/lessons/42884
def solution(routes):
    routes = sorted(routes, key=lambda x: (x[1], x[0]))
    k = routes[0][1]
    print(routes)
    cnt = 1
    for i in range(1, len(routes)):
        if routes[i][0] <= k <= routes[i][0]:
            continue
        else:
            cnt += 1
            k = routes[i][1]
    return cnt