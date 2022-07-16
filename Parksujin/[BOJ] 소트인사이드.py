N = int(input())
num = list(map(int, str(N))) # str형인 N을 다시 int로 바꾼 후 list에 저장
num.sort(reverse = True)
for i in range(len(num)):
  print(num[i], end = '') # end = ''를 통해 한줄로 출력
