# https://school.programmers.co.kr/learn/courses/30/lessons/12973
def solution(s):
    data = [s[0]]
    for x in range(1, len(s)):
        if data:
            if data[-1] == s[x]:
                data.pop()
            else:
                data.append(s[x])
        else:
            data.append(s[x])
    return 0 if data else 1