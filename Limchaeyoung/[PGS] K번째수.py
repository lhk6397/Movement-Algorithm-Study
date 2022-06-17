# https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for x in range(len(commands)):
        new_array = array[commands[x][0]-1:commands[x][1]]
        new_array.sort()
        answer.append(new_array[commands[x][2]-1])
    return answer

# return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))