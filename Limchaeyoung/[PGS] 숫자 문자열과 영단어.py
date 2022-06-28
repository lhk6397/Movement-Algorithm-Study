# https://programmers.co.kr/learn/courses/30/lessons/81301
def solution(s):
    answer = s
    num = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five", "6": "six", "7": "seven",
           "8": "eight", "9": "nine"}
    for key, value in num.items():
        answer = answer.replace(value, key)
    return int(answer)