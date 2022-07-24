def solution(s):
    li=list(s)
    p=0
    y=0

    for i in range(len(li)):
        if str(li[i])=='p' or str(li[i])=='P':
            p+=1
        elif str(li[i])=='y' or str(li[i])=='Y':
            y+=1

    if p==y:
        return True
    elif p==0 and y==0:
        return True
    elif p!=y:
        return False