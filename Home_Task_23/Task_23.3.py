lst = input('введите список чисел: ').split()
print(lst)
res=[]
while len(lst) != 0:
  biggest = 0
  indeks = {}
  for i in lst:
    if int(i[0]) > int(str(biggest)[0]):
      biggest = int(i)
      delet = i
    elif int(i[0]) == int(str(biggest)[0]):
      for j in i:
        if j
  res.append(biggest)
  lst.remove(delet)

print(res)
#33 9 8 19 25 44 2 57 71
#9 9 88 7 16 2 33 4 45 8 9 4
#1 1 1 1 1 1 2 55
#0 0 0 1