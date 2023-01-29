n = int(input())
x = []
for i in range(n):
    y = [1] * (i+1)
    for j in range(1, i):
        y[j] = (x[i-1][j-1]+x[i-1][j])
    x.append(y)
for k in x:
  print(k)