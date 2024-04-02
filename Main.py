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

    start_hour = 12
    start_minute = 3
    end_hour = 12
    end_minute = 12
    i = 1
    total_mileage = 0

    while i < 41:                           # Search by time
        if package_loader.search(i).truck == "Truck Two":
            if package_loader.search(i).start_time > datetime.timedelta(hours=end_hour, minutes=end_minute):
                status = "At Hub"
            elif package_loader.search(i).start_time >= datetime.timedelta(hours=start_hour, minutes=start_minute) or package_loader.search(i).delivery_time > datetime.timedelta(hours=end_hour, minutes=end_minute):
                status = "In Route"
            else:
                status = package_loader.search(i).status

            total_mileage = total_mileage + \
                package_loader.search(i).delivery_mileage

            print(package_loader.search(i).ID, package_loader.search(i).street,
                  package_loader.search(i).city, package_loader.search(i).zip,
                  package_loader.search(
                i).weight, package_loader.search(i).deadline, package_loader.search(i).truck,
                package_loader.search(i).delivery_time, status)

        i += 1

    # print("{:.1f}".format(total_mileage))


if __name__ == "__main__":
    main()
