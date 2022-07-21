# https://programmers.co.kr/learn/courses/30/lessons/17681
def solution(n, arr1, arr2):
    map1 = []
    map2 = []
    final_map = ["0"] * n
    for x in arr1:
        k = str(format(x, 'b'))
        map1.append("0"*(n-len(k)) + k)
    for x in arr2:
        k = str(format(x, 'b'))
        map2.append("0" * (n - len(k)) + k)
    for x in range(n):
        road = ""
        for y in range(n):
            if map1[x][y] == '1' or map2[x][y] == '1':
                road += "#"
            else:
                road += " "
        final_map[x] = road
    return final_map