memo = {0:[0,1,0],1:[1,0,1]} #초기값

def fib(n):
  if n in memo:   #전에 계산된 값이라면,
    return memo[n]    #바로 그값을 리턴

  else:   #처음 계산하는 것이라면,
    tmp = fib(n-1) + fib(n-2)   #두 값과 실행횟수를 리스트에서 넣어
    memo[n] = [0,0,0]

    #메모에 넣어준다
    memo[n][0] = tmp[0] + tmp[3]	#tmp 인덱스 0과 3은 함수계산값
    memo[n][1] = tmp[1] + tmp[4]	#tmp 인덱스 1과 4는 각함수의 0실행횟수를 더함
    memo[n][2] = tmp[2] + tmp[5]	#tmp 인덱스 2과 5는 각함수의 1실행횟수를 더함

    return memo[n]


n = int(input())
for i in range (n):
  n1 = int(input())
  print("%d %d"%(fib(n1)[1],fib(n1)[2]))
