import math
lst = list(map(int,input('Введите cписок чисел через пробел: ').split()))
a = lst[0]
for i in lst[1:]:
  nok = (a*i)//math.gcd(a,i)
  a=nok
print('Наименьшее общее кратное = ',nok)