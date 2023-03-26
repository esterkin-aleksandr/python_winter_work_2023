tree = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8), (8, 9)]
dct = {}
for a, b in sorted(tree):
  dct[b] = dct.get(a, 0) + 1
  print(dct)
print(max(dct.values())+1)