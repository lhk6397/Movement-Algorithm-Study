def solution(array, commands):
    answer = []
    # res = []
    # commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
    for i, j, k in commands:
        ans = array[i - 1: j]
        ans.sort()
        answer.append(ans[k - 1])


    return answer