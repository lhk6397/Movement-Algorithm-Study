# https://school.programmers.co.kr/learn/courses/30/lessons/42839
def solution(numbers):
    number = ''
    for n in numbers:
        number += str(n)
    data = []
    s = []
    visited = [False] * len(numbers)
    dfs(len(number), data, s, visited, numbers)

def dfs(length, data, s, visited, numbers):
    if len(s) == length:
        data.append(int(''.join(map(str, s))))
    for x in range(len(numbers)):
        if visited[x]:
            continue
        visited[x] = True
        s.append(numbers[x])
        dfs(length, data, s, visited, numbers)
        s.pop()
        visited[x] = False
        