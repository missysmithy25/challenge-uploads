#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv 
myfile = 'election_data.csv'
output_file = "election_results.txt"
with open(myfile,'r' ) as election_results:
    reader = csv.reader(election_results,delimiter = ",")
    header_row = next(election_results)
    total_ballots = 0
    candidates = []
    voting_numbers = []
    proportion_list = []
    candidate_count = {}

    for line in reader:
        total_ballots += 1                 #Summing up all of the ballots
        if line[2] not in candidates:
            candidates.append(line[2])       # Adding a new candidate to the candidates list
            candidate_count[line[2]] = 0     # Create a counter for that new candidate 
        candidate_count[line[2]] +=1         # Continue to count votes down the list


    for key in candidate_count:
        proportion = round(candidate_count[key]/total_ballots,2)*100  # get the proportion for each candidate 
        proportion_list.append(proportion)                            # add to list 
        voting_numbers.append(candidate_count[key])                   # add voting numbers for each candidate to list
        sorted_numbers = sorted(voting_numbers)                       # sort the list of voting numbers in ascending order 

    highest_votes = sorted_numbers[len(sorted_numbers)-1]             #retreive the highest voting number 

    
    #Find the key in the dictionary for highest voting number
winner = [name for name, num_votes in candidate_count.items() if num_votes == highest_votes]


    #Election Results
title = "Election Results\n"
print(title)
total = f"Total Votes {total_ballots}\n"
print(total)
for i in range(len(candidates)):
    results = (f"{candidates[i]}: {proportion_list[i]}% ({voting_numbers[i]})")
    print(results)
who_won =f"Winner: {winner[0]}"
print(who_won)

# Export to text file 
with open(output_file, "w") as output_file:
    output_file.write(title)
    output_file.write(total)
    for i in range(len(candidates)):
        results = (f"{candidates[i]}: {proportion_list[i]}% ({voting_numbers[i]})\n")
        output_file.write(results)
    output_file.write(who_won)

        


# In[ ]:




