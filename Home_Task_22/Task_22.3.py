import keyword
y = keyword.kwlist
x = input('Введите строку: ').split()
res = []
for word in x:
  if word in y:
    res.append('<KW>')
  else:
    res.append(word)
print(' '.join(res))
