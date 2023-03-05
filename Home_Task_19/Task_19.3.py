class Person:
  def __init__(self, surname, name, patronim):
    self.surname = surname
    self.name = name
    self.patronim = patronim
  def __str__(self):
    return (self.patronim[::-1] + self.name[::-1] + self.surname[::-1] )

a,b,c = input('Введите ФИО: ').split()
p = Person(a,b,c)
print(p)
