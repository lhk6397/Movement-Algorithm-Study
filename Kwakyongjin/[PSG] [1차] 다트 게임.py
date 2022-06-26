# '*' 과 '#'의 구현 방식이 어려워서 참고해버림...ㅠ
def solution(dartResult):
    num = '' 
    score = []
    for result in dartResult:
        if result.isnumeric(): # isnumeric(): 해당 문자열이 숫자로 이루어져 있나 아닌가 체크
            num += result
        elif result == 'S':
            num = int(num)**1
            score.append(num)
            num = ''
        elif result == 'D':
            num = int(num)**2
            score.append(num)
            num = ''
        elif result == 'T':
            num = int(num)**3
            score.append(num)
            num = ''  
        elif result == '*':
            if len(score) > 1:
                score[-2] *= 2
                score[-1] *= 2
            else:
                score[-1] *= 2
        elif result == '#':
            score[-1] *= -1
    answer = sum(score)
    return answer
