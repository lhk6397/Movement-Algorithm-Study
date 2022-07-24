def solution(s):

    sp_s=s.split(' ')

    for i in range(len(sp_s)):
        li_s=list(sp_s[i])

        for j in range(len(li_s)):
            if j%2==0:
                li_s[j]=li_s[j].upper()
            elif j%2==1:
                li_s[j]=li_s[j].lower()

        sp_s[i]=''.join(li_s)

    answer=' '.join(sp_s)

    return answer