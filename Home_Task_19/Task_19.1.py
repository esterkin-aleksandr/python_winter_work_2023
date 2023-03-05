import itertools
money = [50, 100, 200, 500, 1000, 5000]
lst = []
for x in (itertools.combinations(money, 3)):
  lst.append(sum(list(x)))
print(lst)