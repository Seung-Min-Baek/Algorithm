n,m = map(int,input().split())
a = []
for _ in range(n): # 3x3 행렬 입력을 위해 n행만큼 반복
    k=list(map(int,input().split()))
    a.append(k)
b=[]
for _ in range(n):
    k=list(map(int,input().split()))
    b.append(k)

# 행렬 a,b 덧셈
for i in range(n): 
  for j in range(m):
    print(a[i][j]+b[i][j],end=' ')
  print()
