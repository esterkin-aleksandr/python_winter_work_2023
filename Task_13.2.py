def poly():
  i=1
  while True:
    if(str(i)==str(i)[::-1]):
      yield i
      i+=1
    else:
      i+=1

g = poly()
for x in range(1000):
  print(next(g), end=", ")
