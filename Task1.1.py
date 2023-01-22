x = int (input())
y = int (input())
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
w1 = 0
l1 = 0
w2 = 0
l2 = 0
w3 = 0
l3 = 0
w4 = 0
l4 = 0
lw = 0
if a > b :
  w1 = a
  l1 = b
else:
  w1 = b
  l1 = a
if w1 > c :
  w2 = w1
  l2 = c
else:
  w2 = c
  l2 = w1
if w2 > d :
  w3 = w2
  l3 = d
else:
  w3 = d
  l3 = w2
if w3 > e :
  w4 = w3
  l4 = e
else:
  w4 = e
  l4 = w3
if l1 > l2:
    lw = l1
else:
    lw = l2
if lw < l3:
    lw = l3
if lw < l4:
    lw = l4
print (lw)