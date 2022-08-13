# https://school.programmers.co.kr/learn/courses/30/lessons/42888
def solution(record):
    name_dic = {}
    result = []

    for r in record:
        info = r.split()
        if info[0] in ["Enter", "Change"]:
            name_dic[info[1]] = info[2]

    for r in record:
        info = r.split()
        if info[0] == "Enter":
            result.append(name_dic[info[1]] + "님이 들어왔습니다.")
        elif info[0] == "Leave":
            result.append(name_dic[info[1]] + "님이 나갔습니다.")