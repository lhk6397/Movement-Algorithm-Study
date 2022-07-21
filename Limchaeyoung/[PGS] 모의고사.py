# https://programmers.co.kr/learn/courses/30/lessons/42840
def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = { 1: correct(p1, answers), 2: correct(p2, answers), 3: correct(p3, answers)}
    new_score = sorted(score, key=lambda x: score[x], reverse=True)
    if score[new_score[2]] != score[new_score[1]]:
        del new_score[2]
    if score[new_score[1]] != score[new_score[0]]:
        del new_score[1:]
    return new_score

def correct(p, answers):
    cnt = 0
    for x in range(len(answers)):
        if p[x%len(p)] == answers[x]:
            cnt += 1
    return cnt