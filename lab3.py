import math

def func(x,y):
	func = (x*x)-(2*y)
	return func
a = 0.0
b = 1.0
n = 30

delta_x = (b-a)/n
yExact , yApproxEiler2 , yApproxIE2 , yApproxRK2 ,  = 0 , 0, 0 , 0 
yApproxImprovedEiler , yApproxEiler , yApproxRK = 1.0 ,1.0 , 1.0
x , y = 0 , 0
i = 1
yExact_show ,delta_E , delta_IE , delta_RK = [] , [] , [] , []
while(i<=n): 
	prev_x = x
	prev_y = y
	x = i*delta_x

	yExact = (3.0/4.0*(math.pow(math.e, -2*x)) + (1.0/2.0*x*x) - (1.0/2.0*x) + 1.0/4.0);
	yApproxEiler2 = yApproxEiler
	yApproxEiler = yApproxEiler2 + delta_x+x*func(x,yApproxEiler2)
	yApproxIE2 = yApproxImprovedEiler


	yApproxImprovedEiler = yApproxIE2  + (delta_x/2)*(func(x,yApproxIE2 ) + func(x+delta_x, yApproxIE2  + func(x,yApproxIE2 )*delta_x))
	yApproxRK2 = yApproxRK
	yApproxRK = yApproxRK2 + func(x,yApproxRK2)*delta_x + (func(x+delta_x , yApproxRK2 + (func(x, yApproxRK2))*delta_x)- func(x,yApproxRK2))/delta_x*delta_x*delta_x/2 
	delta_E.append(abs(yExact - yApproxEiler))
	delta_IE.append(abs(yExact - yApproxImprovedEiler))
	delta_RK.append(abs(yExact - yApproxRK))
	yExact_show.append(yExact)
	i+=1
	
SumEiler = sum(delta_E)
SumIE = sum(delta_IE)
SumRK = sum(delta_RK)
print("yExact: " , yExact_show)
print("delta of Eiler:" , delta_E)
print("delta of Improved Eiler:" , delta_IE)
print("delta Runge-Kutta:" , delta_RK)
print("Math expect for Eiler:" , SumEiler/n)
print("Math expect for Improved Eiler:" , SumIE/n)
print("Math expect for RK :" , SumRK/n)