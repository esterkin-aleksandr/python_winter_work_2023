n = int(input())
res=[]
for i in range(1,n+1):
  if n % i == 0:
    res += [i]
print(res)