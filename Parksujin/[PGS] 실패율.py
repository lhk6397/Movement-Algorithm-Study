def solution(N, stages):
    answer = [] 
    fail_st = {}
    cnt = len(stages)
    for j in range(1, N + 1): 
      if cnt != 0:
        fail_st[j] = stages.count(j)/cnt 
        cnt -= stages.count(j)         
      else:           
        fail_st[j] = 0 
      
          
      answer = sorted(fail_st, key = lambda x: fail_st[x], reverse = True)
            
    return answer

