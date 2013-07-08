# -*- coding: cp1252 -*-
# OPEN CSV Data File and List its Header
# List its first 5 and last 5 data elements.
# Get the summary of all the columns in the data file.

import csv as csv 
import numpy as np
import os as os

# Function to clear the screen.
def cls(): print "\n" * 100

# Function to get the summary of CSV data.
def csv_data( data ):

    #print number of elements in this list.
    n = len(data)           #This will give us number of rows.
    print 'Number of lines of csv data read : ', n

    # print full data
    #print data                       #print Data List.

    #print top 5 elements from the data list
    print 'First 5 : ', data[:5]

    #print last 5  elements from the data list
    print 'Last 5 : ', data[n-6:]      

    

############## Start Of the Application ##############
cls()

print ' '

#Open up the csv file in to a Python object
csv_file_object = csv.reader(open('train.csv', 'rb')) 
header = csv_file_object.next()  #The next() command just skips the 
                                 #first line which is a header

print 'File Header : ', header                     #print the header

data=[]                          #Create a variable called 'data'


for row in csv_file_object:      #Run through each row in the csv file
    data.append(row)             #adding each row to the data variable

#csv_data(data)                  # Call our Function.
#print top 5 elements from the data list
#print 'First 5 : ', data[:5]


data = np.array(data) 	         #Then convert from a list to an array
			         #Be aware that each item is currently
                                 #a string in this format
#print type(data)

print ' type of array : ', type(data)
print ' array data type : ', data.dtype

print 'length data : ',len(data)
print 'ndim data : ',data.ndim
print 'shape data : ',data.shape

print ' np data array :\n', data

number_passengers = np.size(data[0::,0].astype(np.float))
number_survived = np.sum(data[0::,1].astype(np.float))
proportion_survivors = number_survived / number_passengers

print ' number_passengers= {%d}, number_survived= {%d}, proportion_survivors = {%f}' % (number_passengers,number_survived, proportion_survivors)

#print data[0::,4]

print 'Women Only Data'
women_data = data[0::,4] == "female"
women_onboard = data[women_data,1].astype(np.float)  #Get Survival Values for Women Only.
#print women_onboard 
print len(women_onboard) 

print 'Men Only Data'
men_data = data[0::,4] != "female"
men_onboard = data[men_data,1].astype(np.float)     #Get Survival Values for men Only.
print len(men_onboard) 


# Proportions of men and women survived.
proportion_women_survived = np.sum(women_onboard) / np.size(women_onboard)  
proportion_men_survived = np.sum(men_onboard) / np.size(men_onboard) 

#and then print it out
print 'Proportion of women who survived is %s' % proportion_women_survived
print 'Proportion of men who survived is %s' % proportion_men_survived



#print 'length data : ',len(women_data)
#print 'ndim data : ',women_data.ndim
#print 'shape data : ',women_data.shape


print '       '
print 'Exit CSV Data reader!'
