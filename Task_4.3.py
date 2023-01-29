a=input()
b=input()
a=a.lower()
b=b.lower()
x = {}
y = {}
for i in a:
  if str(i).isalpha():
    if i not in x:
      x[i] = 0
    x[i] += 1
for j in b:
  if str(j).isalpha():
    if j not in y:
      y[j] = 0
    y[j] += 1
if x == y:
  print('True')
else:
  print('False')