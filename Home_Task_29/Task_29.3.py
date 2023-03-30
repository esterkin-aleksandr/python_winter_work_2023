def isometr(x, y):
  dct1 = {}
  dct2 = {}
  for i,j in enumerate(x):
    if j in dct1:
      if y[i] != dct1[j]:
        return print('Слова не изоморфны!')
    else:
      dct1[j] = y[i]



    if y[i] in dct2:
      if j != dct2[y[i]]:
        return print('Слова не изоморфны!')

    else: dct2[y[i]] = j

  return print('Слова изоморфны!')

isometr('cosas', 'asdrd')