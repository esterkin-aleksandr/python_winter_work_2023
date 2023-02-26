def Title_decorator(fu):
  def wrapper():
    res1 = fu()
    res2 = res1.title()
    return res2
  return wrapper
@Title_decorator
def vvod():
  t = input('Введите текст: ')
  return t
print(vvod())