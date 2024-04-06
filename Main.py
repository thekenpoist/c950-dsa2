# Steve Hull WGU ID# 011096053
# C950 - Data Structures and Algorithms II
# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION

# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The Main module contains the necessary code to launch the program and provide a UI.
# Comments in the code provide information about the program flow


# ***** THE PROGRAM IS LAUNCHED FROM THIS FILE *****


# Import the os module - needed to clear the screen on program launch
import os
# Import the PackageLoader module - needed to create a package loader object to handle the hash table
from PackageLoader import *
# Import the HandleCsv module - needed to create an object to handle reading in the .csv files
from HandleCsv import *
# Import the DeliverPackages module - needed to create the algorithm object to calculate the delivery pattern
from DeliverPackages import *
# Import DisplayManager module - needed to display requested data to the user
from DisplayManager import *


# The name of the .csv file containing the package information
package_file = "PackageFile.csv"
# The name of the .csv file containing the distance between addresses
distance_table = "DistanceTable.csv"


# The main program that gets the ball rolling starts here...
def main():

    # Load the packages into the hash table as Package objects
    handle_csv = HandleCsv(package_file)
    package_loader = PackageLoader(handle_csv.read_csv()).package_loader()

    # Load the distance file into a 2 dimensional array
    handle_csv = HandleCsv(distance_table)
    distance_file = handle_csv.read_csv()

    # Instantiate and call the DeliverPackages class - this is where the processing of the packages on the trucks happens
    deliver_packages = DeliverPackages()
    deliver_packages.deliver_packages(package_loader, distance_file)

    # Instantiate display management object
    display = DisplayManager()


    choice = ""

    # This is where I provide the user with an intuitive interactive interface
    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear') # Clear the screen for easier viewing

        print("Welcome to the WGUPS delivery application...\n")

        # The user has 4 data output choices, or can select 'q' to quit the application
        while choice != '1' or choice != '2' or choice != '3' or choice != '4' or choice != '5':

            print("Select from one of the following options or 'q' to quit:")
            print("1. View package status by ID")
            print("2. View package status by truck")
            print("3. View package status by time")
            print("4. View all package status and total mileage")

            choice = input("Please enter a selection(1-4):")
            if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == 'q':
                break
            else:
                print("Invalid selection\n\n")

        match choice:
            case '1': # Select 1 to view package status by ID
                pack_id = input("Enter a package ID(1-40):")
                display.display_one_package(package_loader, pack_id)
                again = input("\nPress return to continue:")
                
            case '2': # Select 2 to view packages status by truck
                truck_num = input("Enter a truck number(1-3):")
                display.display_by_truck(package_loader, truck_num)
                again = input("\nPress return to continue:")
                
            case '3': # Select 3 to view packages status by time
                hour = input("Enter the hour(0-23):")
                minute = input("Enter the minute(0-59):")
                display.display_by_time(package_loader, hour, minute)
                again = input("\nPress return to continue:")
                
            case '4': # Select 4 to view all packages status and total mileage
                display.display_all_packages(package_loader)
                again = input("\nPress return to continue:")

            case 'q': # Select q to quit
                quit()
    


if __name__ == "__main__":
    main()
