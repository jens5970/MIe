# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:08:49 2020

@author: Magnus Jørgensen
"""
import numpy as np

# input is the 3 x N matrix generated from previous question.
# Statistics is a string for which keyvalue, that need to be computed ex. mean temperature

def dataStatistics(data, statistics):
        # First i make letters in lower case, if people spelled wrong
        stats = statistics.lower() 
        if stats == "mean temperature":
        # Here i make sure the output is defined by what the user want to see
            STATS =  np.mean(data[:,0])
            
            # built in function that calculate mean
            
        elif stats == "mean growth rate":
        # If the wants to see 'mean growth rate'
        
            STATS =  np.mean(data[:,1])
            
        elif stats == "std temperature":
        # If user wants to see standard deviation of temperature
            STATS = np.std(data[:,0]) 
            
            # built in funktion that calculate standard deviation
            
        elif stats == "std growth rate":
        # if user wants to see standard deviation of temperature
            STATS = np.std(data[:,1])
            
        elif stats == "rows":
        # If user wants to see number of rows
        
            STATS = len(data[:,0])
            
            # length of Temperature vector is the number of rows
            
        elif stats == "mean cold growth rate":
        # if user wants to se the mean cold growth rate
        
           Cold_Rate = data[:,0][data[:,0] < 20]
           
        # Here a new array is made that only takes the numbers which is less 
        # than 20 degrees
           STATS = np.mean(Cold_Rate)
        # The mean of the new array is calculated here
           
        elif stats == "mean hot growth rate":
        # If user wants to see 'the mean hot growth rate'
        
            Hot_Rate = data[:,0][data[:,0] > 50]
            
        # Here an array with temperature over 50 is made
        
            STATS = np.mean(Hot_Rate)
            
        # The mean of the new array is calculated
            
        else:
        # Here  comes a warning if the user has spelled the specification wrong
            STATS = "Spelling wrong. Try again"
            
        return STATS # Return the specified statistical value the user wants to see
        
    

    
    
    
            
        
        
