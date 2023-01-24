x = int(input())
lst = []
while x != 0:
   lst.append(x)
   x = int(input())
q = 0
for i in lst:
  q += i
if len(lst) > 0:
   print(f'средняя зарплата = {q / len(lst)}')
else:
  print('средняя зарплата = 0')