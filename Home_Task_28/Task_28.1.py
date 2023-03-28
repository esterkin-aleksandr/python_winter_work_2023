lst = input('Введите список: ').split()
lst = list(map(int, lst))
# lst = [7, 8, 9, 5, 4, 3]
print(lst)
invers = 0
for i in range(len(lst)):
  for j in range(i+1, len(lst)):
    if i < j:
      if lst[i] > lst[j]:
        invers+=1
print(invers)