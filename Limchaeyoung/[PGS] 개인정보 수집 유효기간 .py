# https://school.programmers.co.kr/learn/courses/30/lessons/150370
def solution(today, terms, privacies):
    today = [ int(today[0:4]), int(today[5:7]), int(today[8:10]) ]
    ty, date, answer = dict(), list(), list()
    for term in terms:
        t, y = term.split()
        ty[t] = int(y)
    for pr in privacies:
        n = ty[pr[11]]
        y, m, d = int(pr[0:4]), int(pr[5:7])+n, int(pr[8:10])-1
        while(m>12):
            m-=12
            y+=1
        if d == 0:
            m-=1
            d=28
        date.append((y,m,d))
    for i in range(len(date)):
        yc, mc, dc = today[0] - date[i][0], today[1] - date[i][1], today[2] - date[i][2]
        if yc > 0: answer.append(i+1)
        elif yc < 0: continue
        elif mc > 0: answer.append(i+1)
        elif mc < 0: continue
        elif dc > 0: answer.append(i+1)
    return answer