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

    i = 1
    total_mileage = 0
    while i < 41:
        if package_loader.search(i).truck == "Truck Three":
            total_mileage = total_mileage + \
                package_loader.search(i).delivery_mileage
            print(package_loader.search(i))
        i += 1

    print("{:.1f}".format(total_mileage))


if __name__ == "__main__":
    main()
