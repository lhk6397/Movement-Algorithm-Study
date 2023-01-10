import sys
input = sys.stdin.readline

def dfs(repeats, _index, ans, plus, substract, multiply, divide):
    global max_result
    global min_result

    if repeats == n-1:
        max_result = max(max_result, ans)
        min_result = min(min_result, ans)
        return
    
    if plus:
        dfs(repeats+1, _index + 1, ans + graph[_index], plus - 1, substract, multiply, divide)
    
    if substract:
        dfs(repeats+1, _index + 1, ans - graph[_index], plus, substract - 1, multiply, divide)

    if multiply:
        dfs(repeats+1, _index + 1, ans * graph[_index], plus, substract, multiply - 1, divide)
    
    if divide:
        dfs(repeats+1, _index + 1, int(ans / graph[_index]), plus, substract, multiply, divide - 1)

n = int(input().rstrip())
graph = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_result = -1e9
min_result = 1e9
ans = graph[0]

dfs(0, 1, ans, operators[0], operators[1], operators[2], operators[3])
print(max_result)
print(min_result)
