def solution(board, moves):
    answer = 0
    moks=[]

    def mok(num):
        for i in range(len(board)):
            mine=board[i][num-1]

            if mine!=0:
                board[i][num-1]=0
                return  mine
        return None

    for j in moves:
        k=mok(j)
        print(k)

        if k is not None:
            if len(moks)>0 and moks[-1]==k:
                moks.pop()
                answer+=2
            else:
                moks.append(k)

    return answer