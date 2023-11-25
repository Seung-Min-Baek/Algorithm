arr = []

for _ in range(9):
  arr.append(list(map(int,input().split())))

num = 0
max_row=0
max_col=0
for row in range(9):
  for col in range(9):
    if num <= arr[row][col]:
      num = arr[row][col]
      max_row = row+1
      max_col = col+1

print(num)
print(max_row,max_col)