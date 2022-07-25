import sys

sentence = list(sys.stdin.readline().rstrip())
n = int(sys.stdin.readline())
sentence2 = []

for _ in range(n):
    order = list(sys.stdin.readline().split())

    if order[0] == 'P':
        sentence.append(order[1])
    
    elif order[0] == 'L':
        if sentence:
            sentence2.append(sentence.pop())
        
    elif order[0] == 'D':
        if sentence2:
            sentence.append(sentence2.pop())
    
    elif order[0] == 'B':
        if sentence:
            sentence.pop()

sentence.extend(reversed(sentence2))
print(''.join(sentence))
