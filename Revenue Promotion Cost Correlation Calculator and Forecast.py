#to forecast promotion cost based off of desired revenue, change the z input list

#to change the correlation data, change the path in the wb variables


import numpy as np
from pylab import *
import xlrd as xl
import matplotlib as plt
from sklearn.linear_model import LinearRegression


wb = xl.open_workbook("RB Company Revenue Data Test.xlsx")
sheet = wb.sheet_by_index(0)

row1 = []

for row in range(2, sheet.nrows):
    row1.append(sheet.row_values(row))

rvaluez = row1[0]

rvaluez = np.array(rvaluez).reshape(-1,1)


wb2 = xl.open_workbook("RB Company Promotion Cost Data Test.xlsx")
sheet2 = wb2.sheet_by_index(0)

row2 = []

for row in range(2, sheet2.nrows):
    row2.append(sheet2.row_values(row))


pvalues = row2[0]

pvalues = np.array(pvalues)

linear_model = LinearRegression().fit(rvaluez,pvalues)

r2 = model.score(x,y)

# scatter(rvaluez, pvalues)

rev_wanted= [10000, 100000]

z = np.array(rev_wanted).reshape((-1,1))

prom_pred = model.predict(z)

datalist1 = [1, 2, 3, 4 , 5 , 6]
datalist2 = [3, 5, 7, 9, 11, 13]

x = np.array(datalist1).reshape((-1,1))
y = np.array(datalist2)

model = LinearRegression().fit(x,y)

r_sq = model.score(x, y)

z = np.array([2, 4, 8, 9]).reshape((-1,1))

y_pred = model.predict(z)

y_pred

#scatter(x,y)

