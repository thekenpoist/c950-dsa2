# Steve Hull
# WGU ID# 011096053
# 04/04/2024
# C950 - Data Structures and Algorithms II
# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION

# ***** THE PROGRAM IS LAUNCHED FROM THIS FILE *****

# Import the os module - needed to clear the screen on program launch
import os
# Import the PackageLoader module - needed to create a package loader object to handle the hash table
from PackageLoader import *
# Import the HandleCsv module - needed to create an object to handle reading in the .csv files
from HandleCsv import *
# Import the DeliverPackages module - needed to create the algorithm object to calculate the delivery pattern
from DeliverPackages import *


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

    deliver_packages = DeliverPackages()
    deliver_packages.deliver_packages(package_loader, distance_file)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("Welcome to the WGUPS delivery application.")
    print("Please select from one of the following options:")
    print("1. View package status by ID")
    print("2. View package status by truck")
    print("3. View package status by time")
    print("4. View all package status and total mileage")
    print("5. Quit")

    choice = input("Please enter a selection(1-5):")

    if choice == '5':
        quit()

    elif choice == '1':
        pack_id = input("Enter a package ID(1-40):")
        pack_id = int(pack_id)

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
        print("------------------------------------------------------------------------------------------------------------------------------")

        print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(pack_id).ID, 
                                                                         package_loader.search(pack_id).street,
                                                                         package_loader.search(pack_id).city, 
                                                                         package_loader.search(pack_id).zip,
                                                                         package_loader.search(pack_id).weight, 
                                                                         package_loader.search(pack_id).deadline,
                                                                         package_loader.search(pack_id).truck, 
                                                                         package_loader.search(pack_id).status, 
                                                                         package_loader.search(pack_id).delivery_time))

    elif choice == '2':
        truck_num = input("Enter a truck number(1-3):")
        print("------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
        print("------------------------------------------------------------------------------------------------------------------------------")

        i = 1
        if truck_num == '1':
            while i < 40:
                if package_loader.search(i).truck == "Truck One":
                    print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(i).ID, 
                                                                                     package_loader.search(i).street,
                                                                                     package_loader.search(i).city, 
                                                                                     package_loader.search(i).zip,
                                                                                     package_loader.search(i).weight, 
                                                                                     package_loader.search(i).deadline,
                                                                                     package_loader.search(i).truck, 
                                                                                     package_loader.search(i).status, 
                                                                                     package_loader.search(i).delivery_time))
                i += 1

        if truck_num == '2':
            while i < 40:
                if package_loader.search(i).truck == "Truck Two":
                    print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(i).ID, 
                                                                                     package_loader.search(i).street,
                                                                                     package_loader.search(i).city, 
                                                                                     package_loader.search(i).zip,
                                                                                     package_loader.search(i).weight, 
                                                                                     package_loader.search(i).deadline,
                                                                                     package_loader.search(i).truck, 
                                                                                     package_loader.search(i).status, 
                                                                                     package_loader.search(i).delivery_time))
                i += 1

        if truck_num == '3':
            while i < 40:
                if package_loader.search(i).truck == "Truck Three":
                    print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(i).ID, 
                                                                                     package_loader.search(i).street,
                                                                                     package_loader.search(i).city, 
                                                                                     package_loader.search(i).zip,
                                                                                     package_loader.search(i).weight, 
                                                                                     package_loader.search(i).deadline,
                                                                                     package_loader.search(i).truck, 
                                                                                     package_loader.search(i).status, 
                                                                                     package_loader.search(i).delivery_time))
                i += 1

    elif choice == '3':

        hour = input("Enter the hour(0-23):")
        minute = input("Enter the minute(0-59):")
        hour = int(hour)
        minute = int(minute)
        i = 1

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
        print("------------------------------------------------------------------------------------------------------------------------------")

        while i < 41:
            if package_loader.search(i).start_time > datetime.timedelta(hours=hour, minutes=minute):
                if "Delayed" in package_loader.search(i).notes:
                    status = "Delayed in flight"
                else:
                    status = "At Hub"
            elif datetime.timedelta(hours=hour, minutes=minute) >= package_loader.search(i).start_time and datetime.timedelta(hours=hour, minutes=minute) < package_loader.search(i).delivery_time:
                status = "In Route"
            else:
                status = package_loader.search(i).status

            if status == "Delivered":
                print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18} {}'.format(package_loader.search(i).ID, 
                                                                                 package_loader.search(i).street,
                                                                                 package_loader.search(i).city, 
                                                                                 package_loader.search(i).zip,
                                                                                 package_loader.search(i).weight, 
                                                                                 package_loader.search(i).deadline,
                                                                                 package_loader.search(i).truck, 
                                                                                 status, 
                                                                                 package_loader.search(i).delivery_time))
            else:
                print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:18}'.format(package_loader.search(i).ID, 
                                                                              package_loader.search(i).street,
                                                                              package_loader.search(i).city, 
                                                                              package_loader.search(i).zip,
                                                                              package_loader.search(i).weight, 
                                                                              package_loader.search(i).deadline,
                                                                              package_loader.search(i).truck, 
                                                                              status))

            i += 1


    elif choice == '4':
        i = 1
        total_mileage = 0

        print("------------------------------------------------------------------------------------------------------------------------------")
        print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
        print("------------------------------------------------------------------------------------------------------------------------------")

        while i < 41:
            
            total_mileage = total_mileage + package_loader.search(i).delivery_mileage
            print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(i).ID, 
                                                                             package_loader.search(i).street,
                                                                             package_loader.search(i).city, 
                                                                             package_loader.search(i).zip,
                                                                             package_loader.search(i).weight, 
                                                                             package_loader.search(i).deadline,
                                                                             package_loader.search(i).truck, 
                                                                             package_loader.search(i).status, 
                                                                             package_loader.search(i).delivery_time))
            i += 1

        total_mileage = total_mileage + float(package_loader.search(11096053).delivery_mileage)
        print("Total mileage for all trucks is: {:.1f} miles".format(total_mileage))
    



if __name__ == "__main__":
    main()
