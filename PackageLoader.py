# This module was created by Steve Hull, and is all original code.
# The PackageLoader module contains the necessary code to load the packages from the package file into the hash table. 

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
            packTruck = " "
            packDeliveryTime = " "
            packStartTime = " "
            packMileage = 0
            packStatus = "At Hub"

            p = Packages.Packages(packID, packStreet, packCity, packState, packZip,
                                  packDeadline, packWeight, packNotes, packTruck,
                                  packDeliveryTime, packStartTime, packMileage, packStatus)

            package_hash.insert(packID, p)

        return package_hash
