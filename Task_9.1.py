dct = {'G':'C', 'C':'G', 'A':'T', 'T':'A'}
dnk = input()
rnk = []
for i in dnk:
  if i in dct:
    rnk += dct.get(i)
print("".join(rnk))