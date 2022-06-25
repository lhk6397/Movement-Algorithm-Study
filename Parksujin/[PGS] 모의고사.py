def solution(answers):
    answer = []  # 오름차순으로 승자

    res = [0, 0, 0]  # 정답을 맞힌 개수
    way_1 = [1, 2, 3, 4, 5]
    way_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    way_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    for i in range(len(answers)):
        if way_1[i % 5] == answers[i]:
            res[0] += 1
        if way_2[i % 8] == answers[i]:
            res[1] += 1
        if way_3[i % 10] == answers[i]:
            res[2] += 1

    for j in range(3):
        if res[j] == max(res):
            answer.append(j + 1)

    return answer
