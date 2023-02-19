def numdig(n):
# базовый случай
  if n < 10:
    return 1
# рекурсивный случай
  else:
    return 1 + numdig(n // 10)
print(numdig(int(input('Введите число:'))))