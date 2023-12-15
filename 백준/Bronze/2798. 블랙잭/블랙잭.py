n,m = map(int, input().split())
a = list(map(int,input().split()))

result = []
for i in range(n):
  for j in range(i+1,n):
    for k in range(j+1,n):
      sum = a[i] + a[j] + a[k]
      if sum > m:
        continue
      else:
        result.append(sum)
      
print(max(result))