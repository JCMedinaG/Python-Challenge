import csv
import os
list = os.listdir('../Resources')
file = len(list)

for data in range(file):
    budget_data = os.path.join('..', 'Resources' , 'budget_data.csv')
    Item_Count = 0
    profit_start = 0
    total_profit_change = 0
    total_profit = 0
    profit_change = []
    year = []
    month = []
    profit = []
    date = []

    with open(budget_data,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader, None)
        for row in csvreader: 
            print(row)
            Item_Count = Item_Count + 1
            date.append(row[0])
            profit.append(int(row[1]))
            total_profit =  total_profit + int(row[1])
            profit_end = int(row[1])
            profi_change = profit_end - profit_start
            total_profit_change = total_profit_change + profi_change
            profit_change.append(profi_change)
            splitdate = row[0].split('-')
            month.append(str(splitdate[0]))
            year.append(splitdate[1][-2:])
            profit_start = profit_end
    

    average_profit_change = round(total_profit_change/Item_Count,2)
    greatest_increase = max(profit_change) 
    greatest_decrease = min(profit_change)      
    increase_date = date[profit_change.index(greatest_increase)]
    decrease_date = date[profit_change.index(greatest_decrease)]
    months = len(set(date))

with open("Financial_Analyst_Report_" + str(data + 1) + " .txt " , "w") as text:
         print( "Financial Analysis")
         print( "--------------------------------")
         print( "Total Months:" + str(months))
         print( "Total:" + "$" + str(total_profit))
         print( "Average Change:" + "$" + str(average_profit_change))
         print( "Greatest Increase in Profits:" + str(increase_date) + " ($" + str(greatest_increase) + ")")
         print( "Greatest Decrease in Profits:" + str(decrease_date) + " ($" + str(greatest_decrease) + ")")



         text.write( "Financial Analysis")
         text.write( "--------------------------------")
         text.write( "Total Months:" + str(months))
         text.write( "Total:" + "$" + str(total_profit))
         text.write( "Average Change:" + "$" + str(average_profit_change))
         text.write( "Greatest Increase in Profits:" + str(increase_date) + " ($" + str(greatest_increase) + ")")
         text.write( "Greatest Decrease in Profits:" + str(decrease_date) + " ($" + str(greatest_decrease) + ")")