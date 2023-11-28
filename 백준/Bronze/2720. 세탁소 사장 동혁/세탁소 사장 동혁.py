T = int(input())

change = [25, 10, 5, 1]

for _ in range(T):
  C = int(input())
  rest=[]
  for i in change:
    rest.append(C // i)
    C = C%i
  print(*rest)