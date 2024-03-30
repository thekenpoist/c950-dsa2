from PackageLoader import *
from DistanceBetweenAddresses import *
from HandleCsv import *
from NearestNeighbor import *
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

    # Don't forget this!!!!!!!!!!!!!!!!
    # print(package_loader.search(1))

    # print(package_loader.remove(1))
    # print(package_loader.search(1))
    # package_loader.insert(1, 'f00')
    # print(package_loader.search(1))

    # print(package_loader.search(20).status)

    near_neighbor = NearestNeighbor()
    print(near_neighbor.nearest_neighbor(package_loader, distance_file))

    # i = 0
    # while i < 41:
    # print(package_loader.search(i))
    # i += 1


if __name__ == "__main__":
    main()
