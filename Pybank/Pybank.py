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

#initializing the first row profit/loss value
        if months == 1:
            print('abc')
            first_value = int(row[1])

#obtaining the greatest increase in profits, date and amount       
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row [1])
            month_greatest_increase = row [0]

#obtaining the greatest increase in profits, date and amount     
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row [1])
            month_greatest_decrease = row [0]
    
#calculating the average
    average = (last_value-first_value)/(months-1)

#printing the outputs    
    print ('Number of months is {}'. format(int(months)))
    print ('Total is {}'.format(int(total)))
    print ('Average is {}'.format(float(average)))
    print ('Greatest increase is {} in the month of {}'. format(int(greatest_increase),month_greatest_increase))
    print ('Greatest decrease is {} in the month of {}'. format(int(greatest_decrease),month_greatest_decrease))






   
