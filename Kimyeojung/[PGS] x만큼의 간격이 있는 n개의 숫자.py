def solution(x, n):
    answer = []
    k=x

    for i in range(n):
        answer.append(int(x))
        x+=k

    return answer