#imports
import os
import csv


#make a path that goes to the Data
csvpath = os.path.join('/Users/villa/Desktop/Python-Challenge/PyBank/Resources/budget_data.csv')
                       
#using the csv module open the data files
with open(csvpath) as csv_file:
    budget_data = csv.reader(csv_file, delimiter=',')

#now lets set up the names for the colums and rows
    header_row = next(budget_data)
    
#lets make some lists to evaluate the values x
    all_rows = list(budget_data)
    lists = list(zip(*all_rows))
    months = lists[0]
    profits = [int(p) for p in lists[1]]

#name the variables for Profits and losses
    total_profit_loss = 0
    for row in all_rows:
        total_profit_loss += float(row[1])
               
#get the average change in the profit/losses in the given period
    net_change = [int(profits[n] - profits[n-1]) for n in range(1,len(profits))]
    average_monthly_change = sum(net_change) / len(all_rows) - 1
    
                       
#code that give sthe positive change or the increase
    greatest_monthly_profit = 0
    most_profitable_month = 0
    for row in all_rows:
        if float(row[1]) > greatest_monthly_profit:
            greatest_monthly_profit = float(row[1])
            most_profitable_month = row[0]
            
#now for the decrease or the losses
    greatest_monthly_loss = 0
    least_profitable_month = 0
    for row in all_rows:
        if float(row[1]) > greatest_monthly_loss:
            greatest_monthly_loss = float(row[1])
            least_profitable_month = row[0]
#now print out the results and also export a files with the summary values of profits and losses and aslo the change
    print(f'FINANCIAL SUMMARY')
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(f'Total Months:  {len(all_rows)}')
    
    
    if total_profit_loss > 0: 
        print('Total Profit: ${:,.2f}'.format(total_profit_loss))
    else:
        print('Total Loss: ${:,.2f}'.format(total_profit_loss))
    
    if average_monthly_change > 0:
        print('Average Monthly Change: +${:,.2f}'.format(average_monthly_change))
    else:
        print('Average Monthly Change: ${:,.2f}'.format(average_monthly_change*-1))
        
    print(f'Greatest Monthly Profit: {most_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_profit))
    
    print(f'Greatest Monthly Loss: {least_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_loss))
    
    
#the summary of the final results of the data
    print(f'FINANCIAL SUMMARY', file=open("financial_summary.txt","w"))
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', file=open("financial_summary.txt","a"))
    print(f'Total Months: {len(all_rows)}', file=open("financial_summary.txt","a"))
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', file=open("financial_summary.txt","a"))
    print(f'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~', file=open("financial_summary.txt","a"))
 
     
    if total_profit_loss > 0: 
        print('Total Profit: ${:,.2f}'.format(total_profit_loss))
    else:
        print('Total Loss: ${:,.2f}'.format(total_profit_loss))
    
    if average_monthly_change > 0:
        print('Average Monthly Change: +${:,.2f}'.format(average_monthly_change))
    else:
        print('Average Monthly Change: ${:,.2f}'.format(average_monthly_change*-1))
        
    print(f'Greatest Monthly Profit: {most_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_profit))
    
    print(f'Greatest Monthly Loss: {least_profitable_month} -> ' + '+${:,.2f}'.format(greatest_monthly_loss))
    
























 