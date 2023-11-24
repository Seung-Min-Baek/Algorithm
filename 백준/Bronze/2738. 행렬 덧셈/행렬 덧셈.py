n,m = map(int,input().split())
a = []
for _ in range(n):
    k=list(map(int,input().split()))
    a.append(k)
b=[]
for _ in range(n):
    k=list(map(int,input().split()))
    b.append(k)

for i in range(n):
  for j in range(m):
    print(a[i][j]+b[i][j],end=' ')
  print()