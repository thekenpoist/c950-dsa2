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

    # Currently sorting things out without an algorithm in place
    # this works!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    near_neighbor = NearestNeighbor()
    print(near_neighbor.nearest_neighbor(package_loader, distance_file))

   


    '''
    address1 = package_loader.search(20).street
    address2 = package_loader.search(19).street#$#

    handle_csv = HandleCsv(distance_table)
    distance_file = handle_csv.read_csv()
    distance_between_addreses = DistanceBetweenAddresses()
    
    distance = distance_between_addreses.address_distance(distance_file, address1, address2)
    print(distance)

    '''


if __name__ == "__main__":
    main()
