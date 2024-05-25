# Steve Hull
# C950 - Data Structures and Algorithms II
# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION

# This module was created by Steve Hull, and is all original code.
# The Main module contains the necessary code to launch the program and provide a UI.

# ***** THE PROGRAM IS LAUNCHED FROM THIS FILE *****

import os
from PackageLoader import *
from HandleCsv import *
from DeliverPackages import *
from DisplayManager import *


package_file = "PackageFile.csv"
distance_table = "DistanceTable.csv"


def main():

    handle_csv = HandleCsv(package_file)
    package_loader = PackageLoader(handle_csv.read_csv()).package_loader()

    handle_csv = HandleCsv(distance_table)
    distance_file = handle_csv.read_csv()

    deliver_packages = DeliverPackages()
    deliver_packages.deliver_packages(package_loader, distance_file)

    display = DisplayManager()


    choice = ""

    while True:
        
        os.system('cls' if os.name == 'nt' else 'clear') 

        print("Welcome to the WGUPS delivery application...\n")

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
            case '1': 
                pack_id = input("Enter a package ID(1-40):")
                display.display_one_package(package_loader, pack_id)
                again = input("\nPress return to continue:")
                
            case '2': 
                truck_num = input("Enter a truck number(1-3):")
                display.display_by_truck(package_loader, truck_num)
                again = input("\nPress return to continue:")
                
            case '3': 
                hour = input("Enter the hour(0-23):")
                minute = input("Enter the minute(0-59):")
                display.display_by_time(package_loader, hour, minute)
                again = input("\nPress return to continue:")
                
            case '4': 
                display.display_all_packages(package_loader)
                again = input("\nPress return to continue:")

            case 'q': 
                quit()
    


if __name__ == "__main__":
    main()
