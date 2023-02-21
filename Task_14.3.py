def sandwatch(n):
    print('*' * n)
    if n > 1:
        sandwatch(n - 1)
        print('*' * n)
sandwatch(int(input('Введите число: ')))