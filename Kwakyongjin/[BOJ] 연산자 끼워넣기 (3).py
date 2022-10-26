import sys
input = sys.stdin.readline

def dfs(repeats, plus, substract, multiply, divide):
    global max_result
    global min_result
    global op

    if repeats == n-1:
        cal = ["{}".format(graph[0])]
        for i in range(1, n):
            cal.append(op[i-1])
            cal.append("{}".format(graph[i]))
        cal = ''.join(cal)
        ans = eval(cal)
        
        max_result = max(max_result, ans)
        min_result = min(min_result, ans)
        return
    
    if plus:
        op.append('+')
        dfs(repeats+1, plus - 1, substract, multiply, divide)
        op.pop()
    
    if substract:
        op.append('-')
        dfs(repeats+1, plus, substract - 1, multiply, divide)
        op.pop()
    if multiply:
        op.append('*')
        dfs(repeats+1, plus, substract, multiply - 1, divide)
        op.pop()    
    if divide:
        op.append('//')
        dfs(repeats+1, plus, substract, multiply, divide - 1)
        op.pop()

n = int(input().rstrip())
graph = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_result = -1e9
min_result = 1e9
op = []

dfs(0, operators[0], operators[1], operators[2], operators[3])
print(max_result)
print(min_result)
