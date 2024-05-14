#백준 1181번


#사전순서가 맞는지?
def is_big(x,y):
  if x > y:
    return 1
  elif x<y:
    return 0
  else:
    return -1

#같은 길이의 단어수 반환
def is_same(w,n):
  if len(w[n]) == len(w[n+1]):
    return 1

def change(w,ind,n):
  for i in range(n):
    for j in range(n-1,)


number = int(input(""))
words = []

#단어를 리스트에 입력
for i in range(number):
  words.append(input(""))


#단어 글자수 정렬 ( 버블정렬 )
for i in range(number-1):
  for j in range(number,i+1,-1):
    if (len(words[j-1])<len(words[j-2])):
      tmp = words[j-2]
      words[j-2] = words[j-1]
      words[j-1] = tmp



is_found = [0] * 7
is_same = 0

for i in range(number):
  first_word = words[i]
  for j in range(i+1,number):
    if j == number-1 and i == number-1:
      break
    if first_word == words[j]:
      is_same += 1
  
  is_found[i] = is_same
    
#단어 사전순으로 정렬
for i in range(number):
  if is_found[i] != 0:
    change(words,i,is_found[i])
  





#안해
