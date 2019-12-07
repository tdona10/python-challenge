# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 00:42:07 2019

@author: tdona
"""

# Import libraries(Os and CSV)
import os
import csv

#Load Data
filename = 'election_data.csv'
path = os.path.join('resources', filename)
candidates_list=[]
candidate_votes={}
winner_votes=0
voters_list=[]
with open(path) as data:
    csvreader=csv.DictReader(data,delimiter=",")
    for r in csvreader:
        voters_list.append(r['Voter ID'])
        candidate=r["Candidate"]
        if candidate not in candidates_list:
                candidates_list.append(candidate)
                candidate_votes[candidate] = 1
        else:
                candidate_votes[candidate] += 1
    print(len(candidate_votes))
    
#Summarize Data
tot_votes = len(voters_list) 
candidate_percentage = {
    candidate : candidate_votes[candidate]/tot_votes for candidate in candidates_list}
winner_votes=0
for i in candidate_percentage.items():
    if i[1] > winner_votes:
        winner_votes = i[1]
        winner = i[0]

# Report as a list of rows
Report = []
Report.append('-' * 60)
Report.append('Election Results') 
Report.append('-' * 30)
Report.append(f"Total Votes: {tot_votes }\n")
for candidate in candidates_list:
    Report.append(f"{candidate}:{candidate_percentage[candidate]:.3%} ({candidate_votes[candidate]})\n")
          
Report.append('-' * 30)
Report.append( f"Winner: {winner}\n")
Report.append('-' * 60)

#Print each row from the list a terminal
for r in Report:
        print(r) 

#Print each row from the list to a file
with open('Report_output.txt', 'w') as f:
    f.write("\n".join(str(row) for row in Report))