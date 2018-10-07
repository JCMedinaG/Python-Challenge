import csv
import os

csvpath = os.path.join("../Resources", "election_data.csv")

vote_count = 0
candidates = {}
candidates_percent = {}
winner = " "
winner_count = 0

with open(csvpath, newline = "") as csvfile:
     csvreader = csv.reader(csvfile, delimiter= ",")
     next(csvreader, None)

     for row in csvreader:
         vote_count += 1
         if row [2] in candidates.keys():
             candidates[row[2]] += 1
         else:
             candidates[row[2]] = 1    

for x, value in candidates.items():
    candidates_percent[x] = round((value/vote_count) * 100, 2)

for x in candidates.keys():
    if candidates[x] > winner_count:
        winner = x
        winner_count = candidates[x] 

with open('Election_Results_' + '.txt', 'w') as text:
    print("Election Results") 
    print("------------------------------------") 
    print("Total Votes:" + str(vote_count))
    print("------------------------------------") 
    for x, value in candidates.items():
     print(x + ": " + str(candidates_percent[x]) + "% (" + str(value) + ")")
    print("------------------------------------")    
    print("winner: " + winner)
    print("------------------------------------")

    text.write("Election Results") 
    text.write("-----------") 
    text.write("Total Votes:" + str(vote_count))
    text.write("-----------") 
    for x, value in candidates.items():
     text.write(x + ": " + str(candidates_percent[x]) + "% (" + str(value) + ")")
    text.write("-----------") 
    text.write("winner: " + winner)
    




    
