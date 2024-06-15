memo = {0:[0,1,0],1:[1,0,1]}

def fib(n):
  if n in memo:
    return memo[n]

  else:
    tmp = fib(n-1) + fib(n-2)
    memo[n] = [0,0,0]
    memo[n][0] = tmp[0] + tmp[3]
    memo[n][1] = tmp[1] + tmp[4]
    memo[n][2] = tmp[2] + tmp[5]

    return memo[n]


n = int(input())
for i in range (n):
  n1 = int(input())
  print("%d %d"%(fib(n1)[1],fib(n1)[2]))
