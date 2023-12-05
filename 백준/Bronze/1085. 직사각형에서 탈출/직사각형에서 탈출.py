x,y,w,h = map(int,input().split())

box = [x,y,w-x,h-y]
print(min(box))