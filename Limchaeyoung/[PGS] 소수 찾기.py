# https://school.programmers.co.kr/learn/courses/30/lessons/42839
data = set()
def solution(numbers):
    cnt = 0
    numbers = list(numbers)
    for i in range(1, len(numbers)+1):
        s = []
        visited = [False] * len(numbers)
        dfs(s, visited, i, numbers)
    for d in data:
        if check_prime(d):
            cnt += 1
    return cnt

def dfs(s, visited, i, numbers):
    if len(s) == i:
        if s == '0':
            return
        if int(s[0]) != 0:
            data.add(int(''.join(map(str, s))))
        else:
            try:
                data.add(int((''.join(map(str, s)))[1:]))
            except:
                return
        return
    for x in range(len(numbers)):
        if visited[x]:
            continue
        visited[x] = True
        s.append(numbers[x])
        dfs(s, visited, i, numbers)
        s.pop()
        visited[x] = False

def check_prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if not n % i:
            return False
    return True
