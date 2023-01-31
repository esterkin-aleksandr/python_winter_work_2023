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
p1 = 0
p2 = 0
p3 = 0
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
if a == w4:
    if b > c:
        p1 = b
    else:
        p1 = c
    if p1 > d:
        p2 = p1
    else:
        p2 = d
    if p2 > e:
        p3 = p2
    else:
        p3 = e
if b == w4:
    if a > c:
        p1 = a
    else:
        p1 = c
    if p1 > d:
        p2 = p1
    else:
        p2 = d
    if p2 > e:
        p3 = p2
    else:
        p3 = e
if c == w4:
    if a > b:
        p1 = a
    else:
        p1 = b
    if p1 > d:
        p2 = p1
    else:
        p2 = d
    if p2 > e:
        p3 = p2
    else:
        p3 = e
if d == w4:
    if a > b:
        p1 = a
    else:
        p1 = b
    if p1 > c:
        p2 = p1
    else:
        p2 = c
    if p2 > e:
        p3 = p2
    else:
        p3 = e
if e == w4:
    if a > b:
        p1 = a
    else:
        p1 = b
    if p1 > c:
        p2 = p1
    else:
        p2 = c
    if p2 > d:
        p3 = p2
    else:
        p3 = d
print (p3)
