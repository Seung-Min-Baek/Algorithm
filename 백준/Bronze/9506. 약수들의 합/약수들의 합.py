while True:
  n = int(input())
  if n == -1:
    break

  # 약수 구하기
  box=[]
  for i in range(1,n):
    if n%i==0:
      box.append(i)
  
  # 완전수인지 판별
  if n == sum(box):
    print(n,"=",end=" ")
    print(*box, sep=" + ")
  else:
    print(n,"is NOT perfect.")