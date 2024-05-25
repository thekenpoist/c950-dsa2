# This module was created by Steve Hull, and is all original code.
# The DistanceBetweenAddresses module contains the necessary code to access the distance
# table and return the distance between two addresses in the .csv file.

class DistanceBetweenAddresses:

    def __init__(self):
        pass

    # Read in the distance file and the two addresses
    def address_distance(self, distance_file, address1, address2):

        addr1 = distance_file[0].index(address1)
        addr2 = distance_file[0].index(address2)

        # If the cross reference between the two addresses is an empty field
        # switch the addresses and the number will be found
        # This logic is necessary due to the structure of the C950 Course provided DistanceTable.csv
        if distance_file[addr1][addr2] == "":
            return distance_file[addr2][addr1]
        else:
            return distance_file[addr1][addr2]
