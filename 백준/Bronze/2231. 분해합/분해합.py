n = int(input())

everynum = 0
for i in range(1,n+1):
  num = list(map(int, str(i)))
  everynum = sum(num) + i
  if everynum == n:
    print(i)
    break
  if i == n:
    print(0)