def uv(p):
    on = 0
    off = 0

    for i in range(len(p)):
        if p[i] == '(':
            on += 1
        elif p[i] == ')':
            off += 1

        if on == off:
            return p[:i+1], p[i+1:]

def con(u):
    if u[0]=='(' and u[len(u)-1]==')':
        return True
    else:
        return False


def solution(p):
    answer = ''
    if not p:
        return ''

    u,v=uv(p)

    if con(u)==True:
        return u+solution(v)
    else:
        answer+='('
        answer+=solution(v)
        answer+=')'
        for j in u[1:len(u)-1]:
            if j=='(':
                answer+=')'
            else:
                answer+='('

    return answer