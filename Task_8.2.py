a=[[15,5,3],[2,44,2,4],[3,3,3],[111,333,2,15,15]]
sort_1 = sorted(a,key=len)
for i in a:
  i.sort(reverse=True)
print(sort_1)