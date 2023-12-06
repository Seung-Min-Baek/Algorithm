a,b,c = map(int, input().split())

if sum((a,b,c)) - max((a,b,c)) > max((a,b,c)):
  print(a+b+c)
else:
  maxim = sum((a,b,c)) - max((a,b,c)) - 1
  print(maxim + sum((a,b,c)) - max((a,b,c)))