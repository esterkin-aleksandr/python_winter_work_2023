x = int(input())
y = int(input())
a = x + y
b = x - y
c = x * y
d = x / y
w1 = 0
w2 = 0
w3 = 0
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
print (w3)