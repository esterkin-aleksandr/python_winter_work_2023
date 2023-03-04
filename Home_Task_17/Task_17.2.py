def upper_decorator(fu):
  def wrapper(*args,**kwargs):
    res=[]
    for x in args:
      if type(x) == str:
        res.append(x.upper())
    for y in kwargs:
      if type(kwargs[y]) == str:
        res.append(kwargs[y].upper())
    return res
  return wrapper
@upper_decorator
def fu(*args,**kwargs):
  return
print (fu('abc', 3,'b', 2, a = 99, b=1, d='abadag',e='poiu'))