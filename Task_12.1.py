def minimax(x):
  return [i for i in range(0,len(x)) if x[i] == max(x)], [j for j in range(0,len(x)) if x[j] == min(x)]
x = list(map(int, input().split()))
print (minimax(x))