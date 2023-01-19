x = int(input())
y = int(input())
a = x + y
b = x - y
c = x * y
d = x / y
e = x // y
w1 = 0
w2 = 0
w3 = 0
w4 = 0
if a > b:
    w1 = a
else:
    w1 = b
if w1 > c:
    w2 = w1
else:
    w2 = c
if w2 > d:
    w3 = w2
else:
    w3 = d
if w3 > e:
    w4 = w3
else:
    w4 = e
print (w4)