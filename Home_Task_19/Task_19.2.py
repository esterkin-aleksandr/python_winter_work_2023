class Fibonacci:
  def __init__(self):
    self.x = 1
    self.y = 0
    self.z = 0
  def __iter__(self):
    return self
  def __next__(self):
    self.z = self.x + self.y
    self.x = self.y
    self.y = self.z
    return self.x
fibonacci = Fibonacci()
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))
print(next(fibonacci))