class Shape:
  def __init__(self, colour, square):
    self.colour = colour
    self.square = square
  def set_colour(self, x):
    self.colour = x
  def info_colour(self):
    print(self.colour)
  def set_square(self, x):
    self.square = x
  def info_square(self):
    print(self.square)
a = Shape('green',10)
b = Shape('yellow',150)
c = Shape('red',44)
a.info_colour()
b.set_colour('жёлтый')
b.info_colour()
b.info_square()
c.info_square()
c.set_square('55')
c.info_square()