memo = {1:[1,0,1], 2:[1,1,0]}   #1,2자리수의 이친수

def lee(n):   #이전에 계산한 적이 있다면 바로 결과 리턴
  if n in memo:
    return memo[n]

  tmp = lee(n-1)
  memo[n] = [0,0,0]


  memo[n][0] = tmp[1] *2 + tmp[2]   
  #결과값은 마지막수가 0일때 *2 + 마지막수가 1일때 / 0일때는 1과 0이 둘다올수있기 때문에 *2
  memo[n][1] = tmp[1] + tmp[2]
  #마지막숫자가 0일때의 경우는 0으로 끝난수와 1로끝난수의 더하기
  memo[n][2] = tmp[1]
  #마지막숫자가 1일떄의 경우는 0으로 끝난 수 밖에 없다

  return memo[n]
print(lee(int(input()))[0])   #결과 출력
