
import Packages
from HandleCsv import *
from ChainedHashTable import *


class PackageLoader:
     
    def __init__(self, csv_handler):
        self.csv_handler = csv_handler

    def package_loader(self):
        package_hash = ChainedHashTable()

        for line in self.csv_handler:
            packID = int(line[0])
            packStreet = line[1]
            packCity = line[2]
            packState = line[3]
            packZip = line[4]
            packDeadline = line[5]
            packWeight = line[6]
            packNotes = line[7]
            packStatus = "Hub"

            p = Packages.Packages(packID, packStreet, packCity, packState, packZip,
                        packDeadline, packWeight, packNotes, packStatus)
            #print(p)
            package_hash.insert(packID, p)
        
        print(package_hash.search(33))


def main():


    handle_csv = HandleCsv("PackageFile.csv")
    p_loader = PackageLoader(handle_csv.read_csv())
    p_loader.package_loader()


main()
