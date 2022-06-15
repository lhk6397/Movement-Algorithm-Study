# https://programmers.co.kr/learn/courses/30/lessons/17682
def solution(dartResult):
    answer = 0
    count = 0
    is_zero = True
    score = []
    for index, element in enumerate(dartResult):
      if(is_zero == False):
        is_zero = True
        continue
      elif(element.isdigit()):
        now_score = element
        if(dartResult[index+1] == '0'):
          now_score+=dartResult[index+1]
          is_zero = False
        score.append(int(now_score))
        count+=1
      elif(element == 'D'):
        score[count-1] = pow(score[count-1], 2)
      elif(element == 'T'):
        score[count-1] = pow(score[count-1], 3)
      elif(element == '*'):
        if (count >= 2): 
          score[count-2] *= 2
        score[count-1] *= 2
      elif(element == '#'):
        score[count-1] *= -1
    answer = sum(score)
    return answer
  
  
solution("1D2S0T")