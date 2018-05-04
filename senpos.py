import clr
import math
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *

# прямое произведение
def product(v1, v2):
	result = ()
	for t1 in v1:
		for t2 in v2:
			result += ((t1,t2),)
	return result

#Введенные в этом узле данные сохраняется в виде списка в переменных IN.
Category = IN[0] # игнорируем
if(IN[1] == "S"):Load = 0
else:			 Load = 1
Walls = IN[2]
Ceiling = IN[3]
Height = IN[4]
SysType = IN[5] # A - аналоговая, АА - адресно аналоговая

# ИСХОДНЫЕЕ ДАННЫЕ СП5
Lss_=[1, 2]
Lsw_=[1, 2]
# диапазоны высот:
# 			<3.5	3.5-6	6-10	10-12
# дымовые
Lss_[0] = [9,		8.5,	8,		7.5] 
Lsw_[0] = [4.5,		4,		4,		3.5]
#Тепловые
Lss_[1] = [5,		4.5,	4,		0] 
Lsw_[1] = [2.5,		2,		2,		0]

# 1. Определяем нужные W_ss, W_sw
if(Height < 3.5):
	Lss = Lss_[Load][0]
	Lsw = Lsw_[Load][0]
else:
	if (Height >= 2.5 and Height <= 6 ):
		Lss = Lss_[Load][1]
		Lsw = Lsw_[Load][1]
	else:
		if (Height >= 6 and Height <= 10 ):
			Lss = Lss_[Load][2]
			Lsw = Lsw_[Load][2]
		else:
			if (Height >= 10 and Height <= 12 ):
				Lss = Lss_[Load][3]
				Lsw = Lsw_[Load][3]
			else: 
				if (Height > 12 ):
					Lss = 0
					Lsw = 0

#if (Wss == 0): return 0 # расставить невозможно все плохо

# определяем количество на стенах
sensors = [[], []]
N=[]
i=0
for W in Walls:
	between = (W-2*Lsw)/Lss
	if (between < 0):
		n = math.floor(between)+2
	else:
		n = round(between)+2
	step = W/(n+1) # шаг сетки
	N.append(between)
	
	sensors[i].append(step) #первый датчик на стене
	for j in xrange(2, n+1):
		sensors[i].append(j*step)
	i+=1
# определяем итоговое количество в зависимости от системы
summary = product(sensors[0], sensors[1])
if (len(sensors[0]) == 1 and len(sensors[1]) == 1 and SysType == "A"):
	summary += ((summary[0][0]+0.3, summary[0][1]+0.3),)

#Назначьте вывод переменной OUT.
OUT = summary	