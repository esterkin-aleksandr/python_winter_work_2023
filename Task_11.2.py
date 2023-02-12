import csv
import openpyxl
from openpyxl import Workbook
wb = Workbook()
#wb.save('Task_11.2_xl.xlsx')
ws = wb.active
with open('Task_11.2_csv.csv', 'r', encoding='utf-8') as file:
    rows = csv.reader(file)
    sor_rows = sorted(rows, key = lambda x:(x[3], x[1], x[2]))
    for row in sor_rows:
        ws.append(row)
    summ = 0
    for i in range(len(sor_rows)):
        for j in range(5):
            summ += int(sor_rows[i][4])
print(summ)
ws.append(['Итого',summ])
wb.save('Task_11.2_xl.xlsx')