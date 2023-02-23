res=[]
def dctkey(dct):
  for k,v in dct.items():
    if k == x:
      res.append(v)
    if type (v) == dict:
      dctkey(v)
  return res
dct = {1: 1, 2: 2, 3: {2: {22:{1:3,3:{15:2,2:15}}}, 3: {1: 111, 2: 222, 3: {0: 1111, 1: 2222, 2: 3333}}, 1: 11, 6: 22}}
x = 2
print(dctkey(dct))