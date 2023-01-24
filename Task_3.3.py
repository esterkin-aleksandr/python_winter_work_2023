x = input()
x = x.split()
y = sorted(x, key=len)
for i in y:
 	if len(i) == len(y[-1]):
 	   print(i)