#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 18:23:43 2021

@author: ryanp
"""
import csv
import os

#input data file
csvpath = os.path.join('Resources', 'budget_data.csv')

#output path
outpath = os.path.join('Analysis','budget_analysis.txt')

months = []
profit_loss = []
ave_delta_profit_loss = []
average_change = []


with open(csvpath, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    print(reader)
    csvheader = next(reader)
    print(f"Header: {csvheader}")               

    #calculate number of months   
    for row in reader:
        months.append(row[0])
        profit_loss.append(row[1])
    print(len(months))
    
    #calculate total profit or loss
    profit_loss_int = map(int,profit_loss)
    total_profit_loss = (sum(profit_loss_int))
    print(total_profit_loss)

    #calculate average change in profit/loss
    i = 0
    for i in range(len(profit_loss) - 1):
        profit_loss = int(profit_loss[i+1]) - int(profit_loss[i])
        ave_delta_profit_loss.append(profit_loss)
        
    Total = sum(ave_delta_profit_loss)
    average_change = Total / len(ave_delta_profit_loss)
    print (round(average_change))
   
    #greatest profit increase
    max_inc = max(ave_delta_profit_loss)
    print(max_inc)
    j = ave_delta_profit_loss.index(max_inc)
    month_inc = months[j+1]
    
    #greatest profit decrease
    max_dec = min(ave_delta_profit_loss)
    print(max_dec)
    x = ave_delta_profit_loss.index(max_dec)
    month_dec = months[x+1]

#print output to terminal
print('Financial Analysis of Budget Data'+'\n')
print("Total Months: " + str(len(months))+'\n')
print("Total: $ " + str(total_profit_loss)+'\n')   
print("Average Change: $" + str(round(average_change,2))+'\n')
print(f"Greatest Increase in Profits: {month_inc} (${max_inc})"+'\n')
print(f"Greatest Decrease in Profits: {month_dec} (${max_dec})"+'\n')

file = open(outpath,'w')

#print output to file
file.write('Financial Analysis of Budget Data'+'\n')
file.write("Total Months: " + str(len(months))+'\n')
file.write("Total: $ " + str(total_profit_loss)+'\n') 
file.write("Average Change: $" + str(round(average_change,2))+'\n')
file.write(f"Greatest Increase in Profits: {month_inc} (${max_inc})"+'\n')
file.write(f"Greatest Decrease in Profits: {month_dec} (${max_dec})"+'\n')