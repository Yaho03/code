n = int(input())


memo = {1:1, 2:2, 3:4} # 1,2,3을 만들수있는 경우의수

def plus(n):
  if n in memo:
    return memo[n]
  memo[n] = plus(n-1) + plus(n-2) + plus(n-3)
  #마지막에 1,2,3을 더하는 경우
  return memo[n]


for i in range(n):
  a = int(input())
  print(plus(a))
