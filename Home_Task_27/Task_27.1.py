n = int(input('Введите число от 1 до 18: '))
matrix = [[0 for j in range(n)] for i in range(n)]
if n in range(1, 19):
    if n != 1:
        i = 0
        j = 0
        v = 0
        for k in range(n // 2):
            v += 1
            for j in range(k, n -1-k):
                matrix[i][j] += v
            j += 1
            for i in range(k, n - 1 - k):
                matrix[i][j] += v
            i = i + 1
            for j in range(n - 1 - k, k, -1):
                matrix[i][j] += v
            j = j - 1
            for i in range(n - 1 - k, k, -1):
                matrix[i][j] += v
        if n % 2 != 0:
            j += 1
            matrix[i][j] = v + 1

        for i in range(n):
            for j in range(n):
                print(matrix[i][j], ' ', end='')
            print()
    else:
        print(n)
else:
    print('Введено неправильное число!')