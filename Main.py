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

    near_neighbor = NearestNeighbor()
    print(near_neighbor.nearest_neighbor(package_loader, distance_file))

    # i = 0
    # while i < 41:
    # print(package_loader.search(i))
    # i += 1


if __name__ == "__main__":
    main()
