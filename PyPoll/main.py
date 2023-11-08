#Dependencies
import os
import csv
Votes = 0
Charles = 0
Raymon = 0
Diana = 0
Winner = "winner"
Percentage = "{:.0%}.format(Votes)"

#Opens Election Data
file = open('PollResults.txt','w')
dir =os.path.dirname(__file__)
csvpath = os.path.join(dir,'Resources','election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

#Will skip the Header to read values
    csv_header = next(csvreader)
    #print(f"CSV Header:{csv_header}")

#Reads through rows
    for row in csvreader:

        #Count Votes
        Votes += 1

        #Candidates
        if row[2] == "Charles Casper Stockham":
            Charles += 1
        elif row[2] == "Raymon Anthony Doane":
            Raymon += 1
        else:
            Diana += 1
        if Raymon > Charles + Diana:
            Winner = "Raymon Anthony Doane"
        elif Diana > Charles + Raymon:
            Winner = "Diana DeGette"
        elif Charles > Diana + Raymon:
            Winner = "Charles Casper Stockham"
        else:
            Winner = "No Winner"            

#Writes results to Terminal
print("Election Results")
print("------------------------------")
print("Total Votes: " + str(Votes))
print("------------------------------")
print("Charles Casper Stockham: " + str("{:.2%}".format(Charles/Votes))+ " ("  + str(Charles) + ")")
print ("Raymon Anthony Doane:  " + str("{:.2%}".format(Raymon/Votes))+ " (" +str(Raymon) + ")")
print ("Diana DeGette: " + str("{:.2%}".format(Diana/Votes))+ " (" +str(Diana) + ")")
print("------------------------------")
print("Winner: " + Winner)

#Writes Results to Text file

file.write("Election Results")
file.write("\n------------------------------")
file.write("\n")
file.write("\nTotal Votes: " + str(Votes))
file.write("\n------------------------------")
file.write("\nCharles Casper Stockham: " + str("{:.2%}".format(Charles/Votes))+ " ("  + str(Charles) + ")")
file.write("\nRaymon Anthony Doane:  " + str("{:.2%}".format(Raymon/Votes))+ " (" +str(Raymon) + ")")
file.write("\nDiana DeGette: " + str("{:.2%}".format(Diana/Votes))+ " (" +str(Diana) + ")")
file.write("\n")
file.write("\n------------------------------")
file.write("\nWinner: " + Winner)
file.write("\n------------------------------")

file.close()


