def solution(record):
    answer = []
    station=[]
    user=dict()

    for event in record:
        info=event.split()
        action=info[0]
        id=info[1]
        if action in ('Enter','Change'):
            nickname=info[2]
            user[id]=nickname
        station.append((action,id))

    for event2 in station:
        action=event2[0]
        id=event2[1]
        if action=='Enter':
            answer.append(f'{user[id]}님이 들어왔습니다.')
        elif action=='Leave':
            answer.append(f'{user[id]}님이 나갔습니다.')

    return answer