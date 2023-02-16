lst = list(map(int, input().split()))
def nechet(lst):
  for i in lst:
    if i % 2 != 0:
      yield i
g=nechet(lst)
for s in g:
  print(s, end=" ")