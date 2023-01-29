a,c,b = input().split()
a = float(a)
b = float(b)
if c == '*' :
    print (a * b)
elif c == '+':
    print (a + b)
elif c == '-':
    print (a - b)
elif c == ('/') and b == 0:
    print ('Деление на 0!')
elif c == '/' and b != 0:
    print (a / b)