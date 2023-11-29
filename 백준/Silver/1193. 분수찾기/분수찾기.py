x = int(input())
num = 1

while x>num:
  x -= num
  num += 1

if num%2==1:
  a = num-x+1
  b = x
elif num%2==0:
  a = x
  b = num-x+1

print(f"{a}/{b}")
