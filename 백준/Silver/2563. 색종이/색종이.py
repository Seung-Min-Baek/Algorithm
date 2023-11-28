num = int(input())
area = [[0]*100 for _ in range(100)] # 면적 100*100을 0으로

for _ in range(num):
  x,y = map(int, input().split())

  for i in range(x,x+10): # x축을 반복하면서
    for j in range(y,y+10): # y축을 반복하면서
      area[i][j]=1 # 해당 면적을 1로

counts = 0
for i in range(100):
  counts += area[i].count(1) # 1인 면적 수 세기
print(counts)