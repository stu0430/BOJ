a, b, c = map(int, input().split(":"))
x, y, z = map(int, input().split(":"))

h, m, s = x-a, y-b, z-c
if s < 0:
  s += 60
  m -= 1
if m < 0:
  m += 60
  h -= 1
if h < 0:
  h += 24

print("%02d:%02d:%02d"%(h,m,s))
