n, m = map(int, input().split())
dic={}
for i in range(n):
    dic[i+1] = set()
for j in range(m):
    a, b = map(int,input().split())
    dic[a].add(b)
    dic[b].add(a)


def dfs(start, dic):
    stack = [start]
    visited.append(start)

    while stack:
        node = stack.pop()
        for i in dic[node]:
            if i not in visited:
                visited.append(i)
                stack.append(i)

visited = []
count = 0
for i in range(n):
    if not i+1 in visited:
        dfs(i+1, dic)
        count += 1

print(count)
