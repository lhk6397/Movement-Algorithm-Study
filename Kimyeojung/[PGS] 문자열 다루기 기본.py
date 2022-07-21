def solution(s):
    li=list(s)
    num=0
    for i in range(len(li)):
        if '0'<=str(li[i])<='9':
            num+=1

    if len(li)==4 and num==len(li):
        return True
    elif len(li)==6 and num==len(li):
        return True
    else:
        return False