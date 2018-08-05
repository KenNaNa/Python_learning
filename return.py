import math
def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return (nx,ny)
(x,y) = move(100,100,60,math.pi/6)
print((x,y))

r = move(50,50,60,math.pi/5)
print(r)

[x,y] = move(30,30,40,math.pi/6)
print([x,y])