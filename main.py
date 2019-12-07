# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:08:46 2019

@author: tdona
"""

# Import libraries(Os and CSV)
import os
import csv

#Load Data
filename = 'budget_data.csv'
path = os.path.join('resources', filename)
month_list=[]
profitAndLoss_list=[]
profitAndLoss_tot=0
with open(path) as data:
    csvreader=csv.DictReader(data,delimiter=",")
    for r in csvreader:
        month=r["Date"]
        month_list.append(month)
        profitAndLoss =float(r["Profit/Losses"])
        profitAndLoss_list.append(profitAndLoss)
        profitAndLoss_tot +=profitAndLoss

#Summarize Data
greatest_increase = ["",0]
greatest_decrease = ["",0]
numberOfmonths = len(month_list)

for i in range(1,numberOfmonths):
    tot_profitAndLoss_change = 0
    profitAndLoss_change = profitAndLoss_list[i] - profitAndLoss_list[i-1]
    tot_profitAndLoss_change += profitAndLoss_change
    if profitAndLoss_change > greatest_increase[1]:
        greatest_increase = [month_list[i],profitAndLoss_change]
    if profitAndLoss_change < greatest_decrease[1]:
        greatest_decrease = [month_list[i],profitAndLoss_change]

averageOfchange=tot_profitAndLoss_change/numberOfmonths

# Report as a list of rows
Report = []
Report.append('Financial Analysis \n')
Report.append('-' * 60)
Report.append(f"Total Months: {numberOfmonths }\n")
Report.append(f"Total Revenue: ${round(profitAndLoss_tot)}\n")
Report.append(f"Average Revenue Change: ${round(averageOfchange)}\n")
Report.append(f"Greatest Increase in Revenue:{greatest_increase[0]} (${round(greatest_increase[1])}),\n")
Report.append(f"Greatest Decrease in Revenue:{greatest_decrease[0]} (${round(greatest_decrease[1])}),\n")
Report.append('-' * 60)

#Print each row from the list to a terminal
for r in Report:
        print(r)

#Print each row from the list to a file
with open('output.txt', 'w') as f:
    f.write("\n".join(str(row) for row in Report))
    