# 자료구조 수업에서 배운대로 각 연산자의 우선순위를 고려해서 구현

q = list(input())
stack = []
answer = '' 

# 가장 기본적인 경우: stack이 텅 비어있는 경우에는 사칙연산 무조건 추가
for i in q:
    if i.isalpha(): # 문자 i가 대문자인 경우(아스키 코드 활용)
        answer += i
    elif i == '(': # '('인 경우에는 ')'가 나오기 전까지 모든 연산자를 stack에 추가해야 함
        stack.append(i)
    elif i == ')': # '('전까지 있는 모든 연산자를 차례대로 stakc.pop()함
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.pop() # '('버리기
    elif i == '*' or i == '/': # '*', '/'의 경우 서로의 우선순위는 같고 '+', '-' 보다 우선임을 고려함
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer += stack.pop()
        stack.append(i)
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            answer += stack.pop()
        stack.append(i)

while stack: # stack에 남아있는 나머지 연산자들을 빼서 문자열에 추가
    answer += stack.pop()
print(answer)
