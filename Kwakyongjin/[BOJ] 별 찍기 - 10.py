import sys

def solution(n):
    if n == 1:
        return ['*']
    
    stars = solution(n//3)
    answer = []

    for star in stars:
        answer.append(star*3)
    for star in stars:
        answer.append(star+' '*(n//3)+star)
    for star in stars:
        answer.append(star*3)
    return answer


n = int(sys.stdin.readline().rstrip())
print('\n'.join(solution(n)))
