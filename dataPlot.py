# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 13:03:58 2020

@author: Magnus Jørgensen
"""

import matplotlib.pyplot as plt
import numpy as np

def dataPlot(data): # Input is N x 3 matrix from previous function
    
    new_data = data[data[:,0].argsort()]
    
    # Array of temperature growth and bacteria number
    Temp = new_data[:,0]
    Growth_Rate = new_data[:,1]
    Bacteria = new_data[:,2]

    # Arrays of every type of bacterie ex. if bacteria 1 the array could look like
    # [1,1,1,1] etc.
    
    
    B1 = Bacteria[Bacteria == 1]
    B2 = Bacteria[Bacteria == 2]
    B3 = Bacteria[Bacteria == 3]
    B4 = Bacteria[Bacteria == 4]
    
    # Array of growth rate of the types of bacteria is computed
    
    Bact_Growth1 = Growth_Rate[Bacteria == 1]
    Bact_Growth2 = Growth_Rate[Bacteria == 2]
    Bact_Growth3 = Growth_Rate[Bacteria == 3]
    Bact_Growth4 = Growth_Rate[Bacteria == 4]
    
    
    # Arrays of temperature for each bacteria type
    
    Temp_1 = Temp[Bacteria == 1]
    Temp_2 = Temp[Bacteria == 2]
    Temp_3 = Temp[Bacteria == 3]
    Temp_4 = Temp[Bacteria == 4]
    
    # A function is created that generates the plots when user ask for it
    
    
    def PlotA(Temp_1, Temp_2, Temp_3, Temp_4, Bact_Growth1, Bact_Growth2,Bact_Growth3, Bact_Growth4, B1, B2, B3, B4):
        
        plt.plot( Temp_1, Bact_Growth1, "b*", Temp_1, Bact_Growth1, "b", label = "Salmonella enterica")
        plt.plot( Temp_2, Bact_Growth2, "ro", Temp_2, Bact_Growth2, "r", label = "Bacillus cereu")
        plt.plot( Temp_3, Bact_Growth3, "gv", Temp_3, Bact_Growth3, "g", label = "Listeria")
        plt.plot( Temp_4, Bact_Growth4, "ys", Temp_4, Bact_Growth4, "y", label = "Brochothrix thermosphacta")
        
        # All the different 'Temp vs growth rate' for different bacteria. With points and lines
        
        plt.legend(loc = "best", bbox_to_anchor = (0,-0.1, 1, -0.1), mode = "expand"
                   , ncol = 2)
        plt.grid(linestyle = "--")
        
        # Legend and grid is made
        
        plt.title("Growth rate  vs temperature for different types of bacteria")
        plt.xlabel("Temperature")
        plt.ylabel("Growth rate")
        plt.xlim([10,60])
        
        # main title, x and y titles and x-axis limit is created
        
        plt.show()
        
        plt.hist(B1,facecolor = "b")
        plt.hist(B2,facecolor = "r")
        plt.hist(B3,facecolor = "g")
        plt.hist(B4,facecolor = "y")
        
        # Different histograms of bacteria types
        
        plt.grid(linestyle = "--")

        ind = np.arange(1,5)
    
        plt.xticks(ind, ("Salmonella enterica","Bacillus cereus", "Listeria", "Brochothrix thermosphacta")
                   , rotation = 45)
        
        # tickmarks at 1,2,3,4 is created with name of bacteria, rotated 45 degrees so user can read it better
        
        plt.title("Histogram of different bacterias")
        plt.xlabel("Types of Bacteria")
        plt.ylabel("number of occurrences ")
        
        # title and x and y label created
        
        plt.show()

        return
    
    return PlotA(Temp_1, Temp_2, Temp_3, Temp_4, 
                 Bact_Growth1, Bact_Growth2, Bact_Growth3, Bact_Growth4,
                 B1, B2, B3, B4)
    # Output is Plots of 'Temperature vs Growth Rate' and histogram og occurences of different bacteria types.
