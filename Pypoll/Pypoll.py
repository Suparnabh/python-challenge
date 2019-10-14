# @TODO: Your code here
import os
import csv


#defining the path
file_name = os.path.join('Resources','election_data.csv')

# initializing variables
total_votes = 0
candidate_list = []
khan = 0
correy = 0
li = 0
tooley = 0
percent_khan = 0
percent_correy = 0
percent_li = 0
percent_tooley = 0


#reading the csv file
with open(file_name, mode='r', newline='') as file_obj:
    csv_reader = csv.reader(file_obj,delimiter=",")
        
#not reading the header row    
    next(csv_reader,"NONE")
        
#iterating over rows in csv_reader    
    for row in csv_reader:
        total_votes = total_votes + 1 
        candidate_list.append(row[2]) #creating a list with names of all candidates

#couting number of votes for each candidate     
    khan = candidate_list.count('Khan')
    correy = candidate_list.count('Correy')
    li = candidate_list.count('Li')
    tooley = candidate_list.count("O'Tooley")

#Getting the winner name and value
    winner_dic = {'Khan' : int(khan), 'Correy' : int(correy), 'Li' : int(li), "O'Tooley" : int(tooley)}
    maximum = max(winner_dic, key=winner_dic.get)  # Getting winner value and name
    
#Calculating percentage of votes won for each candidate
    percent_khan = (int(khan)/ int(total_votes))*100
    percent_correy = (int(correy)/ int(total_votes))*100
    percent_li = (int(li)/ int(total_votes))*100
    percent_tooley = (int(tooley)/ int(total_votes))*100

#obtaining unique values of candidates        
    candidate_list = list(dict.fromkeys(candidate_list))
  
#printing the outputs    
    print ('Total Votes: {}'.format(int(total_votes)))
    print(candidate_list)
    print('Khan: {}% ({})'.format(round(percent_khan,3),int(khan)))
    print('Correy: {}% ({})'.format(round(percent_correy,3),int(correy)))
    print('Li: {}% ({})'.format(round(percent_li,3),int(li)))
    print("O'Tooley: {}% ({})".format(round(percent_tooley,3),int(tooley)))
    print('Winner : {}'.format(maximum))
    
 