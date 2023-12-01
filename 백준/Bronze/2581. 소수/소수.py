m = int(input())
n = int(input())

box = []
for i in range(m,n+1):
  if i>1:
    error=0
    for j in range(2,i-1):
      if i%j==0:
        error += 1
    if error ==0:
      box.append(i)

if len(box)==0:
  print(-1)
else:
  print(sum(box))
  print(min(box))
