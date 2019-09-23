# import necessary modules
import numpy as np
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
# read the data
df_all = pd.read_csv('C:/Users/rundong-li/Desktop/物理化学实验/5-络合物稳定常数的的测定/original data/A-lambda.csv')
# select corresponding columns and turn them to lists
lambda_list = df_all['λ (nm)'].tolist()
A1 = df_all['A1'].tolist()
A2 = df_all['A2'].tolist()
A3 = df_all['A3'].tolist()
A4 = df_all['A4'].tolist()
A5 = df_all['A5'].tolist()
A6 = df_all['A6'].tolist()
A7 = df_all['A7'].tolist()
A8 = df_all['A8'].tolist()
A9 = df_all['A9'].tolist()
A10 = df_all['A10'].tolist()
A11 = df_all['A11'].tolist()
B1 = df_all['B1'].tolist()
B2 = df_all['B2'].tolist()
B3 = df_all['B3'].tolist()
B4 = df_all['B4'].tolist()
B5 = df_all['B5'].tolist()
B6 = df_all['B6'].tolist()
B7 = df_all['B7'].tolist()
B8 = df_all['B8'].tolist()
B9 = df_all['B9'].tolist()
B10 = df_all['B10'].tolist()
B11 = df_all['B11'].tolist()
# plot for group 1
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(lambda_list, A1)
ax.plot(lambda_list, A2)
ax.plot(lambda_list, A3)
ax.plot(lambda_list, A4)
ax.plot(lambda_list, A5)
ax.plot(lambda_list, A6)
ax.plot(lambda_list, A7)
ax.plot(lambda_list, A8)
ax.plot(lambda_list, A9)
ax.plot(lambda_list, A10)
ax.plot(lambda_list, A11)
ax.legend(['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11'], fontsize=12)
ax.set_xlabel('Wavelength (nm)', fontname = 'Calibri', fontsize = 18)
ax.set_ylabel('Absorbance (a.u.)', fontname = 'Calibri', fontsize = 18)
plt.title('Absorbance-wavelength curve for the 11 samples in group 1', fontname = 'Calibri', fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
# plot for group 2
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(lambda_list, B1)
ax.plot(lambda_list, B2)
ax.plot(lambda_list, B3)
ax.plot(lambda_list, B4)
ax.plot(lambda_list, B5)
ax.plot(lambda_list, B6)
ax.plot(lambda_list, B7)
ax.plot(lambda_list, B8)
ax.plot(lambda_list, B9)
ax.plot(lambda_list, B10)
ax.plot(lambda_list, B11)
ax.legend(['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10','B11'], fontsize=12)
ax.set_xlabel('Wavelength (nm)', fontname = 'Calibri', fontsize = 18)
ax.set_ylabel('Absorbance (a.u.)', fontname = 'Calibri', fontsize = 18)
plt.title('Absorbance-wavelength curve for the 11 samples in group 2', fontname = 'Calibri', fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
# the x-axis: CM/(CM + CL)
x_list = [round(0.1*i, 2) for i in range(11)]
# find the index where λ = 500nm
index_500 = df_all[df_all['λ (nm)']==500].index.tolist()[0]
original_A_group1 = [
    A1[index_500], A2[index_500], A3[index_500], A4[index_500], A5[index_500], A6[index_500],
    A7[index_500], A8[index_500], A9[index_500], A10[index_500], A11[index_500]
]
# use polynomial to fit the data
c1 = np.polyfit(x_list, original_A_group1, 5)
p1 = np.poly1d(c1)
print(c1)
print(p1)
# define the fitting expression
def Fitting_Group1(x):
    return -11.99*x**5+29.13*x**4-20.49*x**3-0.1061*x**2+3.51*x+0.01154
# x-points for fitting expression
x_fit_points = np.linspace(0,1,1000)
# define the background absorbance function, which should be subtracted from the apparent a.u.
def Background_Group1(x):
    # the slope
    k = (original_A_group1[-1]-original_A_group1[0])/(x_list[-1]-x_list[0])
    # the intercept
    b = original_A_group1[0]
    return k*x+b
# background absorbance list
ba_list_group1 = [Background_Group1(x) for x in x_list]
# plot for apparent absorbance at λ = 500nm, group 1
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x_list, original_A_group1, '-o')
ax.plot(x_fit_points, [Fitting_Group1(x) for x in x_fit_points])
ax.plot(x_list, ba_list_group1, '--*')
ax.legend(['apparent absorbance', 'fitting curve', 'background absorbance'], fontsize = 12)
ax.set_xlabel('$C_{M}/(C_{M}+C_{L})$', fontname = 'Calibri', fontsize = 18)
ax.set_ylabel('Absorbance (a.u.)', fontname = 'Calibri', fontsize = 18)
plt.title('The apparent and background absorbance at λ = 500nm for group 1', fontname = 'Calibri', fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
# the x-axis: CM/(CM + CL)
x_list = [round(0.1*i, 2) for i in range(11)]
# find the index where λ = 500nm
index_500 = df_all[df_all['λ (nm)']==500].index.tolist()[0]
original_A_group2 = [
    B1[index_500], B2[index_500], B3[index_500], B4[index_500], B5[index_500], B6[index_500],
    B7[index_500], B8[index_500], B9[index_500], B10[index_500], B11[index_500]
]
# use polynomial to fit the data
c2 = np.polyfit(x_list, original_A_group2, 5)
p2 = np.poly1d(c2)
print(c2)
print(p2)
# define the fitting expression
def Fitting_Group2(x):
    return -4.104*x**5+10.13*x**4-7.242*x**3-0.1871*x**2+1.428*x+0.00453
# define the background absorbance function, which should be subtracted from the apparent a.u.
def Background_Group2(x):
    # the slope
    k = (original_A_group2[-1]-original_A_group2[0])/(x_list[-1]-x_list[0])
    # the intercept
    b = original_A_group2[0]
    return k*x+b
# background absorbance list
ba_list_group2 = [Background_Group2(x) for x in x_list]
# plot for apparent absorbance at λ = 500nm, group 2
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x_list, original_A_group2, '-o')
ax.plot(x_fit_points, [Fitting_Group2(x) for x in x_fit_points])
ax.plot(x_list, ba_list_group2, '--*')
ax.legend(['apparent absorbance', 'fitting curve', 'background absorbance'], fontsize = 12)
ax.set_xlabel('$C_{M}/(C_{M}+C_{L})$', fontname = 'Calibri', fontsize = 18)
ax.set_ylabel('Absorbance (a.u.)', fontname = 'Calibri', fontsize = 18)
plt.title('The apparent and background absorbance at λ = 500nm for group 2', fontname = 'Calibri', fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()
# rectified absorbance for group 1
ra_list_group1 = [Fitting_Group1(x)-Background_Group1(x) for x in x_fit_points]
# rectified absorbance for group 2
ra_list_group2 = [Fitting_Group2(x)-Background_Group2(x) for x in x_fit_points]
# plot for the rectified absorbance
fig, ax = plt.subplots(figsize=(10,8))
ax.plot(x_fit_points, ra_list_group1)
ax.plot(x_fit_points, ra_list_group2)
ax.plot(np.linspace(0,0.25,100), [0.15 for i in range(100)])
ax.legend(['group 1', 'group 2', 'A = 0.15'], fontsize = 12)
ax.set_xlabel('$C_{M}/(C_{M}+C_{L})$', fontname = 'Calibri', fontsize = 18)
ax.set_ylabel('Absorbance (a.u.)', fontname = 'Calibri', fontsize = 18)
plt.annotate(s = 'A = 0.15', xy = (0.25, 0.15), xytext = (0.27, 0.145), fontsize = 14, fontname = 'Calibri', weight = 'black')
plt.title('The rectified absorbance at λ = 500nm for group 1 and group 2', fontname = 'Calibri', fontsize = 18)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.show()