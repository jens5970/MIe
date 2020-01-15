import numpy as np
from dataLoad import dataLoad
from filterData import filterData
from dataStatistics import dataStatistics
from dataPlot import dataPlot

def inputNumber(prompt):
    # INPUTNUMBER Prompts user to input a number
    #
    # Usage: num = inputNumber(prompt) Displays prompt and asks user to input a
    # number. Repeats until user inputs a valid number.
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    while True:
        try:
            num = float(input(prompt))
            break
        except ValueError:
            pass
    return num

####################################################################
def displayMenu(options):
    # DISPLAYMENU Displays a menu of options, ask the user to choose an item
    # and returns the number of the menu item chosen.
    #
    # Usage: choice = displayMenu(options)
    #
    # Input options Menu options (array of strings)
    # Output choice Chosen option (integer)
    #
    # Author: Mikkel N. Schmidt, mnsc@dtu.dk, 2015
    # Display menu options
    for i in range(len(options)):
        print("{:d}. {:s}".format(i+1, options[i]))
    # Get a valid menu choice
    choice = 0
    while not(np.any(choice == np.arange(len(options))+1)):
            choice = inputNumber("Please choose a menu item: ")
    return choice

###################################################################
### MENU.
### Authors: Magnus Holmsteen Jørgensen (S183804) and Jens Hammershøj Beck (S183829).
# Define menu items
options = np.array(["Load data.", "Filter data.", "Display statistics.", "Generate plots.", "Quit."])
options2 = np.array(["Reset filters.", "Add new filter.", "Back."])
# Define empty name variable
filename = ""
# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(options)
    # Menu item chosen
    # ------------------------------------------------------------------
    # 1. Load data
    if choice == 1:
        # Define filter
        filterChosen = "No filter chosen."
        # Ask user to input name and save it in variable
        while (True):
            try:
                filename = input("Please enter filename: ")
                originalData = dataLoad(filename)
                newData = np.copy(originalData)
                break
            except FileNotFoundError:
                print("File not found. Please try again.")
                pass
            except ValueError:
                print("The file is not as described in the assignment.")
                pass
    # ------------------------------------------------------------------
    # 2. Filter data
    elif choice == 2:
        # Is filename empty?
        if filename == "":
            # Display error message
            print("Error: No data has been loaded.")
        else:
            print("Explanation for the filter function:\nYou choose the bacteria " +
                      "whose data you want to filter.\nThe data where growth " + 
                      "rate is not inbetween the bounderies you define will be removed.\n" + 
                      "The data from the other bacteria will not be affected.\n" + 
                      "If you want, you can add multiple filters.") # Explain the filter
            print(filterChosen)
            if filterChosen == "No filter chosen.":
                while (True):
                    try:
                        filterBac = input("Which bacteria do you want to filter?: ")
                        filterLBound = float(input("What should the lower bound be for the growth rate?: "))
                        filterUBound = float(input("What should the upper bound be for the growth rate?: "))
                        newData = filterData(newData,filterBac,filterLBound,filterUBound)
                        filterChosen = "FILTER: Bacteria: " + filterBac + ". Lowerbound: {:f}. Upperbound: {:f}".format(filterLBound,filterUBound)
                        print(filterChosen)
                        break
                    except UnboundLocalError:
                        print("Error: The bacteria you have entered is not in the data. The four " + 
                              "bacteria are: Salmonella enterica, Bacillus cereus, Listeria and Brochothrix thermosphacta.")
                        print(filterChosen)
                        pass
                    except ValueError:
                        print("Error: The upper and lower bounderies has to be numbers.")
                        print(filterChosen)
                        pass
            else:
                # Display menu options and ask user to choose a menu item
                choice2 = displayMenu(options2)
                # ------------------------------------------------------
                # 2.1. Reset filters
                if choice2 == 1:
                    newData = np.copy(originalData)
                    filterChosen = "No filter chosen."
                # ------------------------------------------------------
                # 2.2. Add new filter
                elif choice2 == 2:
                    while (True):
                        try:
                            filterBac = input("Which bacteria do you want to filter?: ")
                            filterLBound = float(input("What should the lower bound be for the growth rate?: "))
                            filterUBound = float(input("What should the upper bound be for the growth rate?: "))
                            filterChosen = filterChosen + "\n" + "FILTER: Bacteria: " + filterBac + ". Lowerbound: {:f}. Upperbound: {:f}".format(filterLBound,filterUBound)
                            newData = filterData(newData,filterBac,filterLBound,filterUBound)
                            print(filterChosen)
                            break
                        except UnboundLocalError:
                            print("Error: The bacteria you have entered is not in the data. The four " + 
                              "bacteria are: Salmonella enterica, Bacillus cereus, Listeria and Brochothrix thermosphacta.")
                            print(filterChosen)
                            pass
                        except ValueError:
                            print("Error: The upper and lower bounderies has to be numbers.")
                            print(filterChosen)
                            pass
                # ------------------------------------------------------
                # 2.3. Back
                    # Nothing
    # ------------------------------------------------------------------
    # 3. Display statistics
    elif choice == 3:
        if filename == "":
            # Display error message
            print("Error: No data has been loaded.")
        else:
            while (True):
                statistic = input("Please enter which statistic you want: ")
                if dataStatistics(newData, statistic) == "Spelling wrong. Try again":
                    print("Error: The statistic you requested is not in this program. The statistics " +
                          "you can request are: Mean Temperature, Mean Growth rate, Std Temperature, " +
                          "Std Growth rate, Rows, Mean Cold Growth rate and Mean Hot Growth rate.")
                    print(filterChosen)
                else:
                    print(dataStatistics(newData, statistic))
                    print(filterChosen)
                    break
    # ------------------------------------------------------------------
    # 4. Generate plots
    elif choice == 4:
        if filename == "":
            # Display error message
            print("Error: No data has been loaded.")
        else:
            dataPlot(newData)
            print(filterChosen)
    # ------------------------------------------------------------------
    # 5. Quit
    elif choice == 5:
        # End
        print("Goodbye")
        break

