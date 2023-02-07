# https://school.programmers.co.kr/learn/courses/30/lessons/43162#
def dfs(graph, visited, v):
    visited[v] = True
    for i in range(len(graph[v])):
        if not visited[i] and graph[v][i]:
            dfs(graph, visited, i)

def solution(n, computers):
    cnt = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            cnt += 1
            dfs(computers, visited, i)
    return cnt