# @TODO: Your code here
import os
import csv


#defining the path
file_name = os.path.join('Resources','budget_data.csv')

#initializing variables
months = 0
total = 0
greatest_increase = 0
greatest_decrease = 0
first_value = 0
change = 0
average = []
month_greatest_increase = ''
month_greatest_decrease = ''


#reading the csv file
with open(file_name, mode='r', newline='') as file_obj:
    csv_reader = csv.reader(file_obj,delimiter=",")
#not reading the header row    
    next(csv_reader,"NONE")
    
#iterating over rows in csv_reader    
    for row in csv_reader:
        months = months + 1
        total = total + int(row[1])
        last_value = int(row[1])
        change = (last_value - first_value)
        first_value = int(row[1])
                

#initializing the first row profit/loss value
        if months == 1:
            change = 0
            
 #adding change values 
        average.append(int(change))        
            
#obtaining the greatest increase in profits, date and amount       
        if int(change) > greatest_increase:
            greatest_increase = int(change)
            month_greatest_increase = row [0]

#obtaining the greatest increase in profits, date and amount     
        if int(change) < greatest_decrease:
            greatest_decrease = int(change)
            month_greatest_decrease = row [0]
    
#calculating the average
    average = (sum(average)/(len(average)-1))
    

#printing the outputs    
    print ('Total months: {}'. format(int(months)))
    print ('Total: ${}'.format(int(total)))
    print ('Average Change: ${}'.format(float(average)))
    print ('Greatest increase in Profits: {} (${})'. format(month_greatest_increase,int(greatest_increase)))
    print ('Greatest decrease in Profits: {} (${})'. format(month_greatest_decrease,int(greatest_decrease)))






   
