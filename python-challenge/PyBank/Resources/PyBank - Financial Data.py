#!/usr/bin/env python
# coding: utf-8

# In[122]:


import csv
myfile = 'budget_data.csv'
output_file = "financial_analysis.txt"
with open(myfile,'r' ) as budget_data:
    reader = csv.reader(budget_data,delimiter = ",")
    header_row = next(budget_data)
    total_months = []
    monthly_amount = []
    net_changes = []
    sum = 0 
   
    net_total = 0
    for line in reader:
        if line[0] not in total_months:
            total_months.append(line[0]) # total number of months included in the dataset
            monthly_amount.append(line[1])
    
            net_total += int(line[1])  # net total amount (profit/losses) over the entire period
    

    for i in range(len(monthly_amount)-1):
        differences = int(monthly_amount[i]) - int(monthly_amount[i+1])
        net_changes.append(differences)
        i+=1


    for item in net_changes:
        sum += int(item)
    avg = sum/len(net_changes)
    

    sorted_net_changes = sorted(net_changes)

    
    #Greatest Decrease in Profit 
    greatest_increase_index = net_changes.index(sorted_net_changes[0])

    
    
    #Greatest Increase in Profit 
    greatest_decrease_index = net_changes.index(sorted_net_changes[len(net_changes)-1])
 
    
    # Financial Analysis Output 
    
    output = ("Financial Analysis\n"
              f"Total Months: {len(total_months)}\n"
              f"Total: {net_total}\n"
              f"Average Change: {round(avg,2)}\n"
              f"Greatest Decrease in Profits: {total_months[greatest_increase_index + 1]} {sorted_net_changes[0]} \n"
              f"Greatest Increase in Profits: {total_months[greatest_decrease_index + 1]} {sorted_net_changes[len(net_changes)-1]} \n"
                          
             )
    print(output)
            
    # Export to text file
    with open(output_file, "w") as output_file:
        output_file.write(output)


# In[ ]:





# In[ ]:




