def heming(x, y):
  heming = 0
  if len(x) == len(y):
    for i in range(len(x)):
      if x[i] != y[i]:
        heming += 1
    return print (heming)
  else:
    return print('Ошибка ввода! ')

x = input('Введите первую строку: ')
y = input('Введите вторую строку: ')
heming(x,y)