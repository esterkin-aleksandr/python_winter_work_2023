def numsum(n):
  if n == 0:
    return 0
  else:
    return n % 10 + numsum(n // 10)
print(numsum(int(input('Введите число:'))))