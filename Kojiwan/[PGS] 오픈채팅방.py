# https://programmers.co.kr/learn/courses/30/lessons/42888

data_storage = {}

def solution(records):
    answer = []
    for i in range(len(records)):
        [state, user_id, *user_name] = records[i].split()
        if state == "Enter":
            data_storage[user_id] = user_name[0] # 저장소에 id : username 추가
            answer.append(["님이 들어왔습니다.", user_id])
        elif state == "Leave":
            answer.append(["님이 나갔습니다.", user_id])
        else: # CHANGE
            data_storage[user_id] = user_name[0] # 저장소의 id 값에 해당하는 username을 변경
    answer = list(map(lambda x: str(data_storage[x[1]]) + x[0], answer)) # 저장소의 id에 대응하는 username으로 설정 후 문자열 출력
    print(answer)
    return answer

solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"])