import re
st = '10 20 30 40 50 0 -2 -3 -4 -5 0 13 15 1 2 3 999 1000 -10000 -1001 10002 -1002'
print(st)
print(re.findall(r'\d*[02468]|-\d*[02468]', st))