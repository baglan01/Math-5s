import math

def func(x):
	func = math.cos(2*x)
	return func

def der(x):
	func = -2*math.sin(2*x)
	return func
#3.1
def formula1(): 
	n = 10
	delta = 10
	print("formula 3.1 : ")
	while delta >= 0.001:
		sum = 0.0
		x = 0 
		delta_x = 1.0/n
		i = 1 
		x = i*delta_x
		formula = (1/delta_x)*( (1/2)*func(x+delta_x)-(1/2)*func(x-delta_x) )
		delta = abs(der(x)-formula)
		print("in n = ", n , " delta is " , delta)
		n+=1
		i+=1
#3.3
def formula2(): 
	n = 10
	delta = 10
	print("formula 3.3 : ")
	while delta >= 0.001:
		sum = 0.0
		x = 0 
		delta_x = 1.0/n
		i = 1 
		x = i*delta_x
		formula = (1/delta_x)*( (1/2) * func(x-2*delta_x) - 2*func(x-delta_x) + 3/2 *func(x) )
		delta = abs(der(x)-formula)
		print("in n = ", n , " delta is " , delta)
		n+=1
		i+=1
#5.1
def formula3(): 
	n = 10
	delta = 10
	print("formula 5.1 : ")
	while delta >= 0.001:
		sum = 0.0
		x = 0 
		delta_x = 1.0/n
		i = 1 
		x = i*delta_x
		formula = (1/delta_x)*( ((1.0/12.0)*func(x-2*delta_x)) - (8.0/12.0)*func(x-delta_x) + (8.0/12.0)*func(x+delta_x) - (1.0/12.0)*func(x+2*delta_x) )
		delta = abs(der(x)-formula)
		print("in n = ", n , " delta is " , delta)
		n+=1
		i+=1

print(formula1())
print("_____________________")
print(formula2())
print("_____________________")
print(formula3())