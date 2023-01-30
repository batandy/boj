import sys

input=sys.stdin.readline

stack=[]
def push(num):
  stack.append(num)

def pop():
  if not stack:
    print(-1)
  else:
    print(stack.pop())

def size():
  print(len(stack))

def empty():
  if not stack:
    print(1)
  else:
    print(0)

def top():
  if not stack:
    print(-1)
  else:
    print(stack[-1])

num=int(input())
for i in range(num):
  cmd=input().split()
  if cmd[0]=="push":
    push(cmd[1])
  elif cmd[0]=="pop":
    pop()
  elif cmd[0]=="size":
    size()
  elif cmd[0]=="empty":
    empty()
  elif cmd[0]=="top":
    top()
  
  