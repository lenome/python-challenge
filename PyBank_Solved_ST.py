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
        # print(row)
        period.append(row[0]) # Append Time array
        profit.append(int(row[1])) # Append Profit array

#average_change = round(sum(profit)/len(period), 2)
change_in_profit=np.diff(profit) # Compute Change in profit from month-to-month
average_change = round(sum(change_in_profit)/len(change_in_profit), 2)

textfile = open('PyBank-Results.txt', 'w') #declare output text file and open for editing
# file.write('This is a test') 

print("Financial Analysis Compiled by Suraj Thyagaraj"),textfile.write("Financial Analysis Compiled by Suraj Thyagaraj\n")
print("----------------------------------------------"),textfile.write("----------------------------------------------\n")

print(f"Total Months: {len(period)}"), textfile.write("Total Months: %d\n" % (len(period)))
if(sum(profit)<0) :
    print(f"Net Loss : ${sum(profit)}"), textfile.write("Net Loss : %d\n" % (sum(profit)))
else :
    print(f"Net Profit : ${sum(profit)}"), textfile.write("Net Profit : %d\n" % (sum(profit)))

print(f"Average Change : ${average_change}"), textfile.write("Average Change : $%f\n" % average_change)
print(f"Maximum Profit of ${max(profit)} achieved during {period[profit.index(max(profit))]}"), 
textfile.write("Maximum Profit of $%d  achieved during %s\n" % (max(profit),period[profit.index(max(profit))]))
print(f"Largest Loss of ${min(profit)} seen during {period[profit.index(min(profit))]}")
textfile.write("Largest Loss of $%d  seen during %s\n" % (min(profit),period[profit.index(min(profit))]))

#finding index of largest increase in profits
indmax=np.argmax(change_in_profit)
print(f"Greatest Increase in Profits: {period[indmax+1]} ${change_in_profit[indmax]} ") #add 1 to index since differential index trails by 1
textfile.write("Greatest Increase in Profits: %s $%d\n" % (period[indmax+1],change_in_profit[indmax]))
#finding index of largest decrease in profits
indmin=np.argmin(change_in_profit)
print(f"Greatest Decrease in Profits: {period[indmin+1]} ${change_in_profit[indmin]} ") #add 1 to index since differential index trails by 1
textfile.write("Greatest Decrease in Profits: %s $%d\n" % (period[indmin+1],change_in_profit[indmin]))
textfile.close()