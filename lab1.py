import math

n = int(input("Input n : "))
L = 1 
a = 0
b = 1
deltaX = (b-a)/n
x = [1.0]*(n+1)
y = [1.0]*(n+1)
dy = [1.0]*(n+1)
for i in range(0,n+1):
	x[i] = deltaX*i
	y[i] = 2*math.sin(3*x[i])
	dy[i] = 6*math.cos(3*x[i])
dy_l = [1.0]*(n+1)
dy_r = [1.0]*(n)
delta_l = [1.0]*(n+1)
delta_r = [1.0]*(n)
for i in range(0,n):
	dy_r[i] = (2*math.sin(3*(x[i]+deltaX)) - y[i])/deltaX
	delta_r[i] = abs( dy[i]- dy_r[i])
for i in range(0,n+1):
	dy_l[i] = (y[i] - (2*math.sin(3*(x[i]-deltaX))))/deltaX
	delta_l[i] = abs( dy[i]- dy_l[i])
Expl = sum(delta_l)/n
Expr = sum(delta_r)/n
print("Left Math Expectation  : " , Expl)
print("Right Math Expectation :" , Expr)