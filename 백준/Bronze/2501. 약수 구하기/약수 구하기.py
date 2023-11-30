n, k = map(int,input().split())

box = []
for i in range(1,n+1):
  if n%i==0:
    box.append(i)

if k>len(box):
  print(0)
else:
  print(box[k-1])