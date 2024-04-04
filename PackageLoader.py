# This module was created by Steve Hull, WGU ID# 011096053 and is all original code.
# The PackageLoader module contains the necessary code to load the packages from the package file
# into the hash table. Comments in the code provide information about the program flow

# Import the Packages module - needed to create the packages for the hash table
import Packages
# Import the ChainedHashTable module - needed to create the hash table to store the packages
from ChainedHashTable import *


class PackageLoader:

    def __init__(self, csv_handler):
        # Initialize the csv_handler containing the data lines from the .csv file
        self.csv_handler = csv_handler

    def package_loader(self):
        package_hash = ChainedHashTable()  # Instantiate the ChainedHashTable object

        # Below reads in the data from the csv_handler one line at a time and creates a package object
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

            # Insert the package object into the hash table
            package_hash.insert(packID, p)

        # Return the loaded hash table to the calling module - in this instance it's Main()
        return package_hash
