for _ in range(int(input())):
  x = []
  y = []
  for _ in range(int(input())):
    a, b = input().split()
    x.append(int(a))
    y.append(b)
  print(y[x.index(max(x))])
