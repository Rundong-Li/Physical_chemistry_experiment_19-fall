# import necessary modules
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from scipy import stats
# data for C6H12
C6H12 = pd.read_csv('C:/Users/rundong-li/Desktop/物理化学实验/4-凝固点降低法测摩尔质量/original data/C6H12.csv')
# data for C10H8 (C6H12 as solvent)
C10H8 = pd.read_csv('C:/Users/rundong-li/Desktop/物理化学实验/4-凝固点降低法测摩尔质量/original data/C10H8.csv')
# plot for C6H12
fig, ax = plt.subplots(figsize=(10,8))
time_C6H12 = [10*i for i in range(max(len(C6H12['#1']), len(C6H12['#2']), len(C6H12['#3'])))]
ax.plot(time_C6H12, C6H12['#1'], '-^')
ax.plot(time_C6H12, C6H12['#2'], '-8')
ax.plot(time_C6H12, C6H12['#3'], '-*')
ax.set_xlabel('Time (s)', fontname = 'Calibri', fontsize = 16)
ax.set_ylabel('Temperature (°C)', fontname = 'Calibri', fontsize = 16)
ax.legend(['group #1', 'group #2', 'group #3'], fontsize = 14)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.annotate(s = 'T = 6.37 °C', xy = (300, 6.38), xytext = (300, 6.45), arrowprops={"arrowstyle":"->"}, fontsize = 12, weight = 'black')
plt.title('T-t curve for C6H12', fontname = 'Calibri', fontsize = 16)
plt.show()
# fit the data, get a line and use it to find the intersection point
time_C10H8_1 = [10*i for i in range(len(C10H8['#1']))]
stats.linregress(time_C10H8_1[30:], C10H8['#1'][30:])
# the fitting expression
def fit_1(x):
    return -0.0005549450549450529*x+4.465934065934065
# plot for C10H8 #1
fig, ax = plt.subplots(figsize=(10,8))
fit_points_1 = np.linspace(100, 450, 100)
ax.plot(time_C10H8_1, C10H8['#1'], '-o')
ax.plot(fit_points_1, [fit_1(t) for t in fit_points_1])
ax.legend(['scatter plot', 'fitting plot'], fontsize = 14)
ax.set_xlabel('Time (s)', fontname = 'Calibri', fontsize = 16)
ax.set_ylabel('Temperature (°C)', fontname = 'Calibri', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.annotate(s = '(172.44, 4.37)', xy = (172.44, 4.37), xytext = (174, 4.5), arrowprops={"arrowstyle":"->"}, fontsize = 12, weight = 'black')
plt.title('T-t curve for C10H8, group #1', fontname = 'Calibri', fontsize = 16)
plt.show()
# fit the data, get a line and use it to find the intersection point
time_C10H8_2 = [10*i for i in range(len(C10H8['#2']))]
stats.linregress(time_C10H8_2[24:34], C10H8['#2'][24:34])
# the fitting expression
def fit_2(x):
    return -0.0006303030303030281*x+4.441636363636364
# plot for C10H8 #2
fig, ax = plt.subplots(figsize=(10,8))
fit_points_2 = np.linspace(50, 350, 100)
ax.plot(time_C10H8_2, C10H8['#2'], '-o')
ax.plot(fit_points_2, [fit_2(t) for t in fit_points_2])
ax.legend(['scatter plot', 'fitting plot'], fontsize = 14)
ax.set_xlabel('Time (s)', fontname = 'Calibri', fontsize = 16)
ax.set_ylabel('Temperature (°C)', fontname = 'Calibri', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.annotate(s = '(114.05, 4.37)', xy = (114.05, 4.37), xytext = (116, 4.45), arrowprops={"arrowstyle":"->"}, fontsize = 12, weight = 'black')
plt.title('T-t curve for C10H8, group #2', fontname = 'Calibri', fontsize = 16)
plt.show()
# fit the data, get a line and use it to find the intersection point
time_C10H8_3 = [10*i for i in range(len(C10H8['#3']))]
stats.linregress(time_C10H8_3[26:37], C10H8['#3'][26:37])
def fit_3(x):
    return -0.0006636363636363632*x+4.463909090909091
# plot for C10H8 #3
fig, ax = plt.subplots(figsize=(10,8))
fit_points_3 = np.linspace(100, 370, 100)
ax.plot(time_C10H8_3, C10H8['#3'], '-o')
ax.plot(fit_points_3, [fit_3(t) for t in fit_points_3])
ax.legend(['scatter plot', 'fitting plot'], fontsize = 14)
ax.set_xlabel('Time (s)', fontname = 'Calibri', fontsize = 16)
ax.set_ylabel('Temperature (°C)', fontname = 'Calibri', fontsize = 16)
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.annotate(s = '(137.46, 4.373)', xy = (137.46, 4.373), xytext = (139, 4.45), arrowprops={"arrowstyle":"->"}, fontsize = 12, weight = 'black')
plt.title('T-t curve for C10H8, group #3', fontname = 'Calibri', fontsize = 16)
plt.show()
# calculate deltaT
print(f'deltaT = {round(6.37-1/3*(4.37+4.37+4.373), 3)} °C')
# calculate the molecular weight of C10H8
print(f'MB = 20*(1000*0.264/(1.999*20.6)) = {round(20*(1000*0.264/(1.999*20.6)),2)} g/mol')