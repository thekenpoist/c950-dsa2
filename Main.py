from PackageLoader import *
from DistanceBetweenAddresses import *
from HandleCsv import *
from DeliverPackages import *
from PackageLookUp import *


package_file = "PackageFile.csv"
distance_table = "DistanceTable.csv"


def main():

    # Load the packages into the hash table as Package objects
    handle_csv = HandleCsv(package_file)
    package_loader = PackageLoader(handle_csv.read_csv()).package_loader()

    # Load the distance file into a 2 dimensional array
    handle_csv = HandleCsv(distance_table)
    distance_file = handle_csv.read_csv()

    deliver_packages = DeliverPackages()
    deliver_packages.deliver_packages(package_loader, distance_file)

    hour = 10
    minute = 20
    i = 1
    total_mileage = 0

    print("------------------------------------------------------------------------------------------------------------------------------")
    print("ID   Address                                 City              Zip     Weight  Deadline  Truck        Status     Delivery Time")
    print("------------------------------------------------------------------------------------------------------------------------------")

    while i < 41:                           # Search by time
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
                  package_loader.search(i).weight, package_loader.search(i).deadline,
                  package_loader.search(i).truck, status, package_loader.search(i).delivery_time))
        #print("------------------------------------------------------------------------------------------------------------------------------")
        else:
            print('{:2d}   {:39} {:17} {:7} {:7} {:9} {:12} {:10}'.format(package_loader.search(i).ID, package_loader.search(i).street,
                  package_loader.search(i).city, package_loader.search(i).zip,
                  package_loader.search(i).weight, package_loader.search(i).deadline,
                  package_loader.search(i).truck, status))

        i += 1

    # print("{:.1f}".format(total_mileage))


if __name__ == "__main__":
    main()
