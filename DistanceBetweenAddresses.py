
class DistanceBetweenAddresses:

    def __init__(self):
        pass

    def address_distance(self, distance_file, address1, address2):

        addr1 = distance_file[0].index(address1)
        addr2 = distance_file[0].index(address2)

        if distance_file[addr1][addr2] == "":
            return distance_file[addr2][addr1]
        else:
            return distance_file[addr1][addr2]
            

