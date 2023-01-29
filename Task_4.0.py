a, b = input().split()
x = {}
y = {}
for i in a:
    if i not in x:
        x[i] = 0
    x[i] += 1
for j in b:
    if j not in y:
        y[j] = 0
    y[j] += 1
if x == y:
    print('True')
