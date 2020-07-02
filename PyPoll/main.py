#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Dependencies
import os
import csv
#File paths for import and output file
election_csv= os.path.join("Resources", "election_data.csv")
output_file= os.path.join("analysis", "election_analysis.txt")

#Variables to store and track information
total_votes= 0
num_candidates= 0
candidates= []
candidates_votes= {}
winner_name = ''
winner_pct= 0
#Read Files
with open(election_csv, 'r') as csvfile:
    csvReader=csv.reader(csvfile,delimiter= ',')
    
    header= next(csvReader)
    
#Loop through all the rows of data collected    
    for row in csvReader:
#Calculating total of votes       
        total_votes += 1
        num_candidates= row[2]
#Conditional statement to add candidates to list if encountered for first time        
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes[row[2]]= 1
#Otherwise, store as key in dictionary and count and track votes for that key
        else:
            candidates_votes[row[2]]= candidates_votes[row[2]] + 1
#Output file as txtfile
with open(output_file, 'w') as txtfile:
    
    print(f' Election Results')
    txtfile.write(f'\n Election Results\n')
    print(f' ----------------------')
    txtfile.write(f' ----------------------\n')
    print(f' Total Votes: {total_votes}')
    txtfile.write(f' Total Votes: {total_votes}\n')
    print(f' ----------------------')  
    txtfile.write(f' ----------------------\n')
#Loop through dictionary to calculate percentages of each candidate
    for candidates in candidates_votes:
        vote_results= (candidates_votes[candidates]/total_votes) * 100 
#Find winner of election
        if vote_results > winner_pct:
                winner_name= candidates
                winner_pct= vote_results
        print(f' {candidates} {round(vote_results,3)}% ({candidates_votes[candidates]})')
        txtfile.write(f' {candidates} {round(vote_results,3)}% ({candidates_votes[candidates]})\n')
    print(f' ----------------------')
    txtfile.write(f' ----------------------\n')
    print(f' Winner: {winner_name} ')
    txtfile.write(f' Winner: {winner_name}\n')
    print(f' ----------------------')
    txtfile.write(f' ----------------------\n')


# In[ ]:




