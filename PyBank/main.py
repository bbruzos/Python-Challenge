#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Import Dependencies
import os
import csv
#File paths for import and output file
pybank_csv= os.path.join("Resources","budget_data.csv")
output_file= os.path.join("analysis", "budget_analysis.txt")
#Variables to store and keep track of values
total_months= 0
profit_losses= 0
revenue_change= 0
total_revenue_change= 0
prev_month= ""
prev_revenue= 0
greatest_increase= 0
greatest_decrease= 0
    
#Open and read csvfile
with open(pybank_csv, 'r') as csvfile: 
    csvReader=csv.reader(csvfile, delimiter= ',')
    
    header= next(csvReader)
  
    for row in csvReader: 
        total_months += 1
        profit_losses += int(row[1])
    
        revenue_change= int(row[1]) - prev_revenue
        
        if total_months > 1: 
            total_revenue_change += revenue_change
            
        if (revenue_change > greatest_increase):
            greatest_increase= revenue_change
            greatest_increase_month = row[0]
       
        if (revenue_change < greatest_decrease):
            greatest_decrease= revenue_change
            greatest_decrease_month= row[0]
    
    average_change= total_revenue_change/(total_months-1)
    
with open(output_file, 'w') as txtfile:        
        
    print(" Financial Analysis")
    txtfile.write("\n Financial Analysis\n")
    print(" -------------------------")
    txtfile.write(" -------------------------\n")
    print(f' Total Months: {total_months}')
    txtfile.write(f' Total Months: {total_months}\n')
    print(f' Total: ${profit_losses}')
    txtfile.write(f' Total: ${profit_losses}\n')
    print(f' Average Change: ${average_change}')
    txtfile.write(f' Average Change: ${average_change}\n')
    print(f' Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})')
    txtfile.write(f' Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n')
    print(f' Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})')
    txtfile.write(f' Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n')
 
            


# In[9]:





# In[ ]:





# In[ ]:





# In[ ]:




