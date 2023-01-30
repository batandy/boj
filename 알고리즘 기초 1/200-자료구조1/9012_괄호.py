n=int(input())

def check_vps():
  vps=list(input())
  stack=[]
  for bracket in vps:
    if len(stack)==0:
      if bracket==')':
       return -1
      stack.append(bracket)
    elif stack[-1]!=bracket:
      stack.pop()
    else:
      stack.append(bracket)
  if not stack:
    return 1
  else:
    return -1
  
for i in range(n):
  if check_vps()==1:
    print('YES')
  else:
    print('NO')
