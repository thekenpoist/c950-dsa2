# Steve Hull
# WGU ID# 011096053
# 04/04/2024
# C950 - Data Structures and Algorithms II
# NHP3 TASK 2: WGUPS ROUTING PROGRAM IMPLEMENTATION

# ***** THE PROGRAM IS LAUNCHED FROM THIS FILE *****

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

    hour = 14
    minute = 20
    i = 1
    total_mileage = 0

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
    print("------------------------------------------------------------------------------------------------------------------------------")

    while i < 41:
        if package_loader.search(i).start_time > datetime.timedelta(hours=hour, minutes=minute):
            status = "At Hub"
        elif datetime.timedelta(hours=hour, minutes=minute) >= package_loader.search(i).start_time and datetime.timedelta(hours=hour, minutes=minute) < package_loader.search(i).delivery_time:
            status = "In Route"
        else:
            status = package_loader.search(i).status

        total_mileage = total_mileage + \
            package_loader.search(i).delivery_mileage

        if status == "Delivered":
            print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10} {}'.format(package_loader.search(i).ID, package_loader.search(i).street,
                  package_loader.search(i).city, package_loader.search(i).zip,
                  package_loader.search(
                      i).weight, package_loader.search(i).deadline,
                  package_loader.search(i).truck, status, package_loader.search(i).delivery_time))
        # print("------------------------------------------------------------------------------------------------------------------------------")
        else:
            print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10}'.format(package_loader.search(i).ID, package_loader.search(i).street,
                  package_loader.search(i).city, package_loader.search(i).zip,
                  package_loader.search(
                      i).weight, package_loader.search(i).deadline,
                  package_loader.search(i).truck, status))

        i += 1
    total_mileage = total_mileage + \
        float(package_loader.search(11096053).delivery_mileage)
    print("Total mileage for all trucks is: {:.1f} miles".format(
        total_mileage))
    print(package_loader.search(11096053).notes)


if __name__ == "__main__":
    main()
