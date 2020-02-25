import os
import csv
import numpy as np #import this module to compute differential 

#Import raw data
data_csv = os.path.join("Resources", "budget_data.csv")

# Lists to store time, profit information
period = []
profit = []

# Open and read csv
with open(data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)
    #print(f"Header: {csv_header}")

    # Read through each row of data after the header
    for row in csvreader:
        period.append(row[0]) # Append Time array
        profit.append(int(row[1])) # Append Profit array

#average_change = round(sum(profit)/len(period), 2)
change_in_profit=np.diff(profit) # Compute Change in profit from month-to-month
average_change = round(sum(change_in_profit)/len(change_in_profit), 2)

print("Financial Analysis Compiled by Suraj Thyagaraj")
print("----------------------------------------------")

print(f"Total Months: {len(period)}")
if(sum(profit)<0) :
    print(f"Net Loss : ${sum(profit)}")
else :
    print(f"Net Profit : ${sum(profit)}")
print(f"Average Change : ${average_change}")
print(f"Maximum Profit of ${max(profit)} achieved during {period[profit.index(max(profit))]}")
print(f"Largest Loss of ${min(profit)} seen during {period[profit.index(min(profit))]}")

#finding index of largest increase in profits
indmax=np.argmax(change_in_profit)
print(f"Greatest Increase in Profits: {period[indmax+1]} ${change_in_profit[indmax]} ") #add 1 to index since differential index trails by 1
#finding index of largest decrease in profits
indmin=np.argmin(change_in_profit)
print(f"Greatest Decrease in Profits: {period[indmin+1]} ${change_in_profit[indmin]} ") #add 1 to index since differential index trails by 1