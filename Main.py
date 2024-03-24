from PackageLoader import *
from AddressDistance import *
from HandleCsv import *


package_file = "PackageFile.csv"
distance_table = "DistanceTable.csv"


def main():

    # Load the packages into the hash table as Package objects
    handle_csv = HandleCsv(package_file)
    package_loader = PackageLoader(handle_csv.read_csv())
    # package_table = p_loader.package_loader()

    # print(package_loader.package_loader().search(19).street)
    # print(package_loader.package_loader().search(12).street)
    address1 = package_loader.package_loader().search(19).street
    address2 = package_loader.package_loader().search(12).street

    handle_csv = HandleCsv(distance_table)

    distance_file = handle_csv.read_csv()

STEVE, IT'S THE INDEX YOU NEED TO LOOK AT!!!

    
    if distance_file[address1][address2] == "":
        print(distance_file[address2][address1])
    else:
        print(distance_file[address1][address2])



if __name__ == "__main__":
    main()
