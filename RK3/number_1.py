import math
x = float(input())
y = float(input())
alpha = float(input())
print('x = ', x * math.cos(alpha) - y * math.sin(alpha), '\ny = ',
      x * math.sin(alpha) + y * math.cos(alpha))
