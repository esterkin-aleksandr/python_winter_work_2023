res=[]
def dctkey(dct):
  for k,v in dct.items():
    if type (v) == dict:
      dctkey(v)
    else:
      if k==1:
        res.append(v)
  return res
dct = {1:{1:{1:{2:1, 1:3333}}}, 2:2, 3:{2:22, 3:{1:111, 2:222, 3:{0:1111, 1:2222, 2:3333}}, 1:{1:{1:55, 3:44}, 2:999}}, 6:22, 15:{16:{3:1, 2:2, 1:888}}}
x = 1
print(dctkey(dct))