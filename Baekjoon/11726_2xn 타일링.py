nemo = {1:1,2:2}  # 2x1,2x2 사이즈를 만드는 경우의수

def nemo2(n):
  if (n in nemo):	#전에 계산한 적이 있다면 결과값 리턴
    return nemo[n]
  
  nemo[n] = nemo2(n-1) + nemo2(n-2)		#2x(n-2)에서 1x2 사이즈 블럭두개
  return nemo[n]						#2x(n-1)에서 2x1 사이즈 블럭하나


n = int(input())
print(nemo2(n) % 10007)
