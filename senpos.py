import clr 
import math 
clr.AddReference('ProtoGeometry') 
from Autodesk.DesignScript.Geometry import * 

# прямое произведение 
def product(v1, v2): 
    result = () 
    for t1 in v1: 
        for t2 in v2: 
            result += ((t1,t2), ) 
    return result 

# ИСХОДНЫЕЕ ДАННЫЕ СП5 
Lss_=[1, 2] 
Lsw_=[1, 2] 
# диапазоны высот: 
#             <3.5    3.5-6    6-10    10-12 
# дымовые 
Lss_[0] = [9,        8.5,    8,        7.5] 
Lsw_[0] = [4.5,        4,        4,        3.5] 
#Тепловые 
Lss_[1] = [5,        4.5,    4,        0] 
Lsw_[1] = [2.5,        2,        2,        0] 

buf =[] 
for i in IN: 
    if isinstance(i, list): 
        buf.append(i) 
    else: 
        buf.append([i]) 

ret = [] 
SysType = buf[3] # A - аналоговая, АА - адресно аналоговая 
for i in xrange(0, len(IN[0])): 
    # Ввод исходных данных 
    if buf[0][i] == "Дым": 
        Load = 0 
    elif buf[0][i] == "Тепло": 
        Load = 1 
    else: 
        ret.append([]) 
        continue 
    Walls = buf[1][i] 
    OUT = buf[2][i] 
    Height = int(buf[2][i])/1000 
     
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
    # линейное произведение 
    summary = product(sensors[0], sensors[1]) 
    # определяем итоговое количество в зависимости от системы 
    if len(sensors[0]) == 1 and len(sensors[1]) == 1 and SysType == ["A"]: 
        summary += ((summary[0][0]+0.3, summary[0][1]+0.3), ) 
    ret.append(summary) 

#Назначьте вывод переменной OUT. 
OUT = ret
