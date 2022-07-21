def solution(seoul):
    answer = ''

    li_seoul=list(seoul)
    x=li_seoul.index('Kim')

    answer='김서방은 '+str(x)+'에 있다'

    return answer