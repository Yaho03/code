nemo = {1:1,2:3} #초기화값

def nemo2(n):
  if (n in nemo):		#전에 계산한경우 결과값 리턴
    return nemo[n]
  
  nemo[n] = nemo2(n-1) + nemo2(n-2)  * 2		#2x(n-2)에서 2x2모양이 두개이므로  *2
  return nemo[n]


n = int(input())
print(nemo2(n) % 10007)
