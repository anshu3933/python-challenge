import os
import pandas as pd
import numpy as np 
import csv


#define variables
months = 0
line_count = 0
valuelist = []

# Read file
csvpath = os.path.join('budget_data.csv')

with open(csvpath, newline = '') as csvfile: 

    csvreader = csv.reader(csvfile, delimiter = ',')
#Calculate total number of months in the dataset
    for row in csvreader:
        if line_count == 0:
            line_count += 1
        else:
                months = line_count
                line_count += 1 
                valuelist.append(row[1])
#Calculate net total profit/loss over the period 
net_profit = sum(int (i) for i in valuelist)
print("months: ", months)
print(net_profit)
#Calculate average change
odd_valuelist = [valuelist[i] for i in range(len(valuelist)) if i % 2 != 0]
even_valuelist = [valuelist[i] for i in range(len(valuelist)) if i % 2 == 0]
sum_change = [int(odd_valuelist[i]) + int(even_valuelist[i]) for i in range(len(odd_valuelist))]
av_change = [i / 2 for i in sum_change]
average_change = sum(av_change)/86 
print(average_change)
#Calculate increase in profits over the period
increased_profits = []
increased_profits = [int(valuelist[i + 1]) - int(valuelist[i]) for i in range(len(valuelist) - 1)]
increased_profits.sort()
print("The largest increase in profit over the period was: ", increased_profits[-1])
#Greatest decrease over the period
print("The largest decrease in revenue over the period was: ", increased_profits[0])
#Print to text
with open("results.txt", "w") as f:
    f.write('Financial Analysis' + '\n' + '-------------------' + '\n' + 'Total Months: %d' % months + '\n' + 'Total: %d' % net_profit + '\n' + 'Average Change: %d' % average_change + '\n' + 'Greatest increase in profits: %d' % increased_profits[-1] + '\n' + 'Greatest Decrease in Profits: %d' % increased_profits[0])
    f.close()