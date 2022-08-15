def solution(clothes):
    answer = 1
    arr={}
    for i in clothes:
        value=i[0]
        key = i[1]

        if key in arr:
            arr[key].append(value)
        else:
            arr[key]=[value]

    for i in arr.keys():
        answer=answer*(len(arr[i])+1)

    return answer-1