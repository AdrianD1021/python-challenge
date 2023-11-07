
#Dependencies
import os
import csv
#Calls Statistcs library
import statistics

#Writes Text File
file = open('BudgetResults.txt','w')

#Declared Variables

TotalMonths = []
TotalProfit = []
TProfit = 0
TMonth = 0
Average = 0
#Declares Revenue Average
RevAverage = []
Changes = []
Months = []
Best = ''
Worst = ''
Max = 0
Min = 0

#Opens Budget Data
csvpath = os.path.join('..','Resources',"C:/Users/adria/Desktop/Rutgers Bootcamp/python-challenge/PyBank/Resources/budget_data.csv")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    #print (csvreader)=

#Will skip the header to read values
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")
#Reads through rows
    for row in csvreader:

        #Counts Months
        TotalMonths.append(row[0])
        TMonth += 1

        #Will add up total Profit
        TotalProfit.append(int(row[1])) 

      
        
        #Creates Array of Values for next Loop to collect Average Changes
        Changes.append(int(row[1]))
        #Creates Array of Months
        Months.append(str(row[0]))

#Second loop to calculate the average changes and puts into new array

for row2 in range(len(Changes)-1):
    #Revenue Calculation Change 
    Change = (Changes[row2+1] - Changes[row2])
    #Collects all changes and puts into RevAverage
    RevAverage.append(Change)

    #Calculating the Average Change using Statistics Library
    Average = statistics.mean(RevAverage)

#Figures out Max and Min Value and Month
for row3 in range(len(RevAverage)):
    if RevAverage[row3] > Max:
        Max = RevAverage[row3]
        Best = Months[row3 +1]
    elif RevAverage[row3] < Min:
        Min = RevAverage[row3]
        Worst = Months[row3 +1]

#Print Financial Data to Terminal
print("Financial Analysis")  
print("---------------------------------")  

#Adds up and Prints Months

print("Total Months:" + str(TMonth))

#Adds up and Prints Total Profit
TProfit = sum(TotalProfit)
print("Total: $" + str("{:.2f}".format(TProfit)))

#Average change print out to 2 decimal places

print("Average Change: $" + str("{:.2f}".format(Average)))

#Calculates and Prints Max and Min Change
print("Greatest Increase in Profits: " + str(Best) + " ($" + str("{:.2f}".format(Max))+ ")")
print("Greatest Decrease in Profits: " + str(Worst) + " ($" + str("{:.2f}".format(Min))+")")

#Prints Financial Data to Text File

      #Print Financial Data to Terminal
file.write("Financial Analysis")  
file.write("\n---------------------------------")  

#Adds up and Prints Months

file.write("\nTotal Months:" + str(TMonth))

#Adds up and Prints Total Profit
TProfit = sum(TotalProfit)
file.write("\nTotal: $" + str("{:.2f}".format(TProfit)))

#Average change print out to 2 decimal places

file.write("\nAverage Change: $" + str("{:.2f}".format(Average)))

#Calculates and Prints Max and Min Change
file.write("\nGreatest Increase in Profits: " + str(Best) + " ($" + str("{:.2f}".format(Max))+ ")")
file.write("\nGreatest Decrease in Profits: " + str(Worst) + " ($" + str("{:.2f}".format(Min))+")")  

