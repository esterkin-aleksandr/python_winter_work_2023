import calendar
year = 2023
lst = []
for month in range(1,13):
    count = 0
    for day in range(1, calendar.monthrange(year, month)[1] + 1):
        dw = calendar.weekday(year, month, day)
        if dw == 3:
            count+=1
            if count ==3:
                lst.append((year,month,day))
print(lst)