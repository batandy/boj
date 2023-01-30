n =int(input())

sent=[]
for i in range(n):
  sent = input().split()
  for let in sent:
    print(let[::-1], end=" ")