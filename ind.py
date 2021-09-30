print("введенные значения должны быть положительными")
print("введите радиус")
r=int(input())
print("введите координату х0")
x0=int(input())
print("введите координату у0")
y0=int(input())
print("введите координату х")
x=int(input())
print("введите координату у")
y=int(input())

if r>0 and x0>=0 and y0>=0 and x>=0 and y>=0:
	if (x*x+y*y)**0.5>r:
		print ("не попали в мишень")
	if (x*x+y*y)**0.5<=r:
		print ("попали в мишень")
	if x==x0 and y==y0:
		print ("попали в центр мишени")
else:
	print ("неверный формат")