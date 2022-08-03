# https://school.programmers.co.kr/learn/courses/30/lessons/60057
def solution(s):
    length = len(s)
    for l in range(1, len(s)//2+1): # 문자열 길이의 반이 넘으면 압축되지 않으므로 문자열 길이의 반까지 반복
        result = ''
        cnt = 1 # 반복된 번수
        for i in range(l, len(s)+l, l):
            if s[i-l:i] == s[i:i+l]:
                cnt += 1
            else:
                if cnt == 1:
                    result += s[i-l:i]
                else:
                    result += str(cnt)+s[i-l:i]
                cnt = 1
        if length > len(result):
            length = len(result)
    return length

# solution("abcabcabcabcdededededede")