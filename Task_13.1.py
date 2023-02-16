def plusminus():
  i=1
  while True:
    if i % 2 == 0:
      yield -i
      i+=1
    else:
      yield i
      i+=1
g = plusminus()
for i in range(100):
  print(next(g), end=", ")
