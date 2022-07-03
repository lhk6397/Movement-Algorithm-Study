# https://programmers.co.kr/learn/courses/30/lessons/42586
import collections
def solution(progresses, speeds):
    answer = []
    days = []
    for x in range(len(progresses)):
        if (100-progresses[x])%speeds[x]==0:
            days.append((100-progresses[x])//speeds[x])
        else:
            days.append((100-progresses[x])//speeds[x] + 1)
    for x in range(len(days)-1):
        if days[x] > days[x+1]:
            days[x+1] = days[x]
    cnt = collections.Counter(days)
    return [x[1] for x in sorted(cnt.items())]

'''
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
'''