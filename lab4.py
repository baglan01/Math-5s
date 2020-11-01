import math

def func(x):
	return math.pow(math.e, x)*math.sin(3*x)

a = 1.0
b = 3.0
tmax = 5.0
c = 0.8

Nt , Nx = 30 , 30
delta_X = (b-a)/Nx;
delta_T = tmax/Nt;

Uapp_1 , Uapp_2 , Uapp_3 , Uapp_4 = [[0] * Nx for i in range(Nx)] , [[0] * Nx for i in range(Nx)] , [[0] * Nx for i in range(Nx)] , [[0] * Nx for i in range(Nx)]

sum1 , sum2 , sum3 , sum4 = 0 , 0 , 0 , 0

Uex = [[0] * 100 for i in range(100)]
x = [0]*100
t = [0]*100

for i in range(0,Nx):
	x[i] = a +(i*delta_X)
for j in range(0,Nx):
	t[j] = (j*delta_T)

for i in range(0,Nx):
	for j in range(0,Nx): 
		Uex[i][j] = func(x[i] - c*t[j])

for i in range(0,Nx):
	 Uapp_1[i][0] = func(x[i])
for i in range(0,Nx):
	 Uapp_2[i][0] = func(x[i])
for i in range(0,Nx):
	 Uapp_3[i][0] = func(x[i])
for i in range(0,Nx):
	 Uapp_4[i][0] = func(x[i])

#Formulas
for i in range(0,Nx-1):
	for j in range(0,Nt-1): 
		Uapp_1[i][j+1] = Uapp_1[i][j] - (c*(Uapp_1[i+1][j] - Uapp_1[i][j])*(delta_T/delta_X))

for i in range(0,Nx-1):
	for j in range(0,Nt-1): 
		Uapp_2[i][j+1] = Uapp_2[i][j] - (c*(Uapp_2[i][j] - Uapp_2[i-1][j])*(delta_T/delta_X))

for i in range(0,Nx-1):
	for j in range(0,Nt-1): 
		Uapp_3[i][j+1] = Uapp_3[i][j] - (c*delta_T/(2.0*delta_X)*(Uapp_3[i+1][j] - Uapp_3[i-1][j]))
for i in range(0,Nx-1):
	for j in range(0,Nt-1): 
		Uapp_4[i][j+1] = ((Uapp_4[i+1][j] + Uapp_4[i-1][j])/2) -(c*delta_T/(2.0*delta_X)*(Uapp_4[i+1][j] - Uapp_4[i-1][j]))

#MA
for i in range(0,Nx-1):
	delta1 = abs(Uex[i][1] - Uapp_1[i][1])
	sum1 += delta1
Ma1 = sum1/Nx
for i in range(0,Nx-1):
	delta2 = abs(Uex[i][1] - Uapp_2[i][1])
	sum2 += delta2
Ma2 = sum2/Nx
for i in range(0,Nx-1):
	delta3 = abs(Uex[i][1] - Uapp_3[i][1])
	sum3 += delta3
Ma3 = sum3/Nx
for i in range(0,Nx-1):
	delta4 = abs(Uex[i][1] - Uapp_4[i][1])
	sum4 += delta4
Ma4 = sum4/Nx

print("Math expect for 1st method:" , Ma1)
print("Math expect for 2nd method:" , Ma2)
print("Math expect for 3rd method:" , Ma3)
print("Math expect for 4th method:" , Ma4)
