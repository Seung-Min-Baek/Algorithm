N, B = map(int,input().split())

digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

rest = []
while N != 0:
  x = N//B # 몫
  rest.append(digit[N%B]) # 나머지
  N=x
  
for i in range(len(rest)-1,-1,-1):
  print(rest[i],end='')