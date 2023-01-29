def d(n):
  res = n
  while (1):
    res += n % 10
    n = int(n / 10)
    if n < 10:
      res += n
      return res


cre = []
for i in range(0, 10001):
  cre.append(d(i))
i = 1
while (i < 10000):
  if i not in cre:
    print(i)
  i += 1
