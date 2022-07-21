# https://programmers.co.kr/learn/courses/30/lessons/17682#
import math
def solution(dartResult):
    answer = []
    for x in range(len(dartResult)):
        if '0' <= dartResult[x] <= '9':
            if len(dartResult) >= 2:
                if dartResult[x] == '0':
                    if dartResult[x-1] == '1':
                        del answer[-1]
                        answer.append(10)
                        continue
            answer.append(int(dartResult[x]))
        elif dartResult[x] == 'D':
            answer[-1] = math.pow(answer[-1], 2)
        elif dartResult[x] == 'T':
            answer[-1] = math.pow(answer[-1], 3)
        elif dartResult[x] == '*':
            if len(answer) >= 2:
                answer[-2] *= 2
            answer[-1] *= 2
        elif dartResult[x] == '#':
            answer[-1] = -answer[-1]
    return sum(answer)