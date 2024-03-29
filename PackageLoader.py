import Packages
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
            packMileage = 0
            packDeliveryTime = 0
            packStatus = "At Hub"

            p = Packages.Packages(packID, packStreet, packCity, packState, packZip,
                                  packDeadline, packWeight, packNotes, packMileage, 
                                  packDeliveryTime, packStatus)

            package_hash.insert(packID, p)
            
        #print(type(package_hash))
        return package_hash
