def calculate_slope(x1, y1, x2, y2):
  if x1 == x2:
    return float('inf')
  elif y1 == y2:
    return 0
  else:
    return (y2 - y1) / (x2 - x1)


def validate_equation_of_line(m, x1, y1, x, y):
  if m == float('inf'):
    return x == x1

  elif m == 0:
    return y == y1
  else:
    b = y1 - m * x1
    return y == m * x + b


T = int(input())  # Number of test cases
for t in range(1, T + 1):
  N = int(input())
  coordindates = []
  for n in range(1, N + 1):
    X, Y = map(int, input().split())
    coordindates.append([X, Y])
  x1, y1 = coordindates[0]
  x2, y2 = coordindates[1]
  m = calculate_slope(x1, y1, x2, y2)
  numberOfAntsToBeMoved = 0-
  for i in coordindates[2:]:
    x, y = i
    if validate_equation_of_line(m, x1, y1, x, y):
      pass
    elif not validate_equation_of_line(m, x1, y1, x, y):
      numberOfAntsToBeMoved += 1
  print(f"Case #{t}: {numberOfAntsToBeMoved}")


