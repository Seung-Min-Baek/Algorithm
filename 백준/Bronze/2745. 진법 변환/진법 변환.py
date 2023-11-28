N, B = input().split()
N = ''.join(reversed(N)) # N의 자리에 맞게 곱해지는 지수가 파이썬 index와 역순관계라 N을 뒤집는다.

digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

sum = 0
for i in range(len(N)-1,-1,-1): # 4 3 2 1 0 순으로 계산
  sum += digit.index(N[i])*(int(B)**i) # ex) 35*36**4

print(sum)