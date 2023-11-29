N = int(input())
room, num = 1, 1

while N>room:
  room += 6*num
  num += 1

print(num)