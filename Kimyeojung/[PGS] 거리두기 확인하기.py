def check(i):
    li_p=[]
    for y in range(5):
        for x in range(5):
            if i[y][x]=='P':
                li_p+=[(y,x)]

    for y,x in li_p:
        for y2,x2 in li_p:
            dist=abs(y2-y)+abs(x2-x)
            if dist==0 or dist>2:
                continue

            if dist==1:
                return 0
            elif y==y2 and i[y][int((x+x2)/2)]!='X':
                return 0
            elif x==x2 and i[int((y+y2)/2)][x]!='X':
                return 0
            elif y!=y2 and x!=x2:
                if i[y][x2]!='X' or i[y2][x]!='X':
                    return 0

    return 1


def solution(places):
    answer = []

    for i in places:
        answer.append(check(i))

    return answer