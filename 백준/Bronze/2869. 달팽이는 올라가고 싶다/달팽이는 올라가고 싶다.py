A,B,V = map(int,input().split())

day = (V-B)/(A-B)
print(int(day) if day==int(day) else int(day)+1)

## 처음시도 때 시간초과 된 반복문 코드
#A,B,V = map(int,input().split())
#num=0

#while V>0:
#  V=V-A
#  num+=1
#  if V==0:
#    break
#  V=V+B

#print(num)
