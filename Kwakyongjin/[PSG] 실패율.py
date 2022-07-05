def solution(N, stages):
    answer = {} # 리스트를 사용하면 Runtime error가 발생한다(시간 초과)
    users = len(stages)
    
    for i in range(1, N+1):
        if users != 0:
            answer[i] = stages.count(i) / users
            users -= stages.count(i)
        else:
            answer[i] = 0
    
    return sorted(answer, key=lambda x: answer[x], reverse=True) # 람다를 이용한 정렬 기억하기
