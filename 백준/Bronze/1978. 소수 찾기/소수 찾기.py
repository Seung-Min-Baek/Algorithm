n = int(input())
prime_num = list(map(int,input().split()))

a=0
box = []
for i in prime_num:
  error = 0
  if i>1:
    for j in range(2,i-1):
      if i%j == 0:
        error +=1
    if error == 0:
      a += 1
  

print(a)